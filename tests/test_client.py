import unittest
from unittest import mock

import requests

from omarthing import Client, OmarThingError


class Resp:
    def __init__(self, status=200, body=None, headers=None):
        self.status_code, self._body, self.headers = status, body, headers or {}

    def json(self):
        if self._body is None:
            raise ValueError("not json")
        return self._body


def client(*responses, **kw):
    s = mock.Mock()
    s.get.side_effect = list(responses)
    return Client("K", session=s, **kw), s


class ClientTests(unittest.TestCase):
    def test_returns_data_and_drops_none_params(self):
        c, s = client(Resp(200, {"status": "success", "request_id": "r1", "data": {"a": 1}}))
        self.assertEqual(c.profile(username="tiktok", format=None), {"a": 1})
        _, kw = s.get.call_args
        self.assertEqual(kw["params"], {"username": "tiktok"})
        self.assertEqual(kw["headers"], {"X-API-Key": "K"})
        self.assertEqual(c.last_request_id, "r1")

    def test_error_body_raises(self):
        c, _ = client(Resp(403, {"status": "error", "code": "KEY_EXPIRED", "message": "expired", "request_id": "r2"}))
        with self.assertRaises(OmarThingError) as cm:
            c.profile(username="x")
        self.assertEqual((cm.exception.status_code, cm.exception.code), (403, "KEY_EXPIRED"))

    def test_retries_429_then_succeeds(self):
        c, s = client(Resp(429, {"status": "error", "code": "RATE", "message": "slow"}, {"Retry-After": "0"}),
                      Resp(200, {"status": "success", "data": {"ok": True}}))
        self.assertEqual(c.usage(), {"ok": True})
        self.assertEqual(s.get.call_count, 2)

    def test_gives_up_after_retries(self):
        bad = Resp(502, {"status": "error", "code": "BAD", "message": "x"}, {"Retry-After": "0"})
        c, s = client(bad, bad, bad)
        with self.assertRaises(OmarThingError):
            c.usage()
        self.assertEqual(s.get.call_count, 3)

    def test_non_json_raises(self):
        c, _ = client(Resp(200, None))
        with self.assertRaises(OmarThingError):
            c.usage()

    def test_connection_error_is_retried_then_raised(self):
        s = mock.Mock()
        s.get.side_effect = requests.ConnectionError("down")
        c = Client("K", session=s, retries=1)
        with mock.patch("omarthing.client.time.sleep"):
            with self.assertRaises(requests.ConnectionError):
                c.usage()
        self.assertEqual(s.get.call_count, 2)

    def test_missing_key(self):
        with mock.patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                Client()


if __name__ == "__main__":
    unittest.main()
