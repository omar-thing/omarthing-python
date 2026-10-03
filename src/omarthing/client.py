"""Minimal client for the Omar-Thing unofficial TikTok API."""
import os
import time

import requests

from ._endpoints import _Endpoints

DEFAULT_BASE_URL = "https://dev.omar-thing.site"
_RETRY_STATUS = {429, 502, 503, 504}


class OmarThingError(Exception):
    """The API answered with an error (or something that is not JSON)."""

    def __init__(self, status_code, code, message, request_id=None):
        super().__init__(f"[{status_code}] {code}: {message}")
        self.status_code = status_code
        self.code = code
        self.message = message
        self.request_id = request_id


class Client(_Endpoints):
    """
    >>> from omarthing import Client
    >>> api = Client("YOUR_API_KEY")          # or set OMARTHING_API_KEY
    >>> api.profile(username="tiktok", format="clean")["followers"]
    """

    def __init__(self, api_key=None, base_url=None, timeout=60,
                 retries=2, session=None):
        self.api_key = api_key or os.environ.get("OMARTHING_API_KEY")
        if not self.api_key:
            raise ValueError("pass api_key=... or set the OMARTHING_API_KEY environment variable")
        self.base_url = (base_url or os.environ.get("OMARTHING_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.session = session or requests.Session()
        self.last_request_id = None

    def _get(self, endpoint, **params):
        """Call /api/v1/<endpoint>; return the response `data`, raise OmarThingError on failure."""
        params = {k: v for k, v in params.items() if v is not None}
        url = f"{self.base_url}/api/v1/{endpoint}"
        headers = {"X-API-Key": self.api_key}
        for attempt in range(self.retries + 1):
            try:
                # never follow redirects: the key header would be forwarded to the new host
                r = self.session.get(url, params=params, headers=headers, timeout=self.timeout,
                                     allow_redirects=False)
            except (requests.ConnectionError, requests.Timeout):
                if attempt == self.retries:
                    raise
                time.sleep(2 ** attempt)
                continue
            if r.status_code in _RETRY_STATUS and attempt < self.retries:
                try:
                    wait = min(float(r.headers.get("Retry-After", 2 ** attempt)), 30)
                except ValueError:
                    wait = 2 ** attempt
                time.sleep(wait)
                continue
            break
        if 300 <= r.status_code < 400:
            raise OmarThingError(r.status_code, "REDIRECT", "unexpected redirect, not following it")
        try:
            body = r.json()
        except ValueError:
            raise OmarThingError(r.status_code, "BAD_RESPONSE", "response was not JSON") from None
        self.last_request_id = body.get("request_id") if isinstance(body, dict) else None
        if r.status_code >= 400 or (isinstance(body, dict) and body.get("status") == "error"):
            raise OmarThingError(
                r.status_code, body.get("code") or "ERROR",
                body.get("message") or body.get("error") or "request failed", self.last_request_id)
        return body.get("data", body)
