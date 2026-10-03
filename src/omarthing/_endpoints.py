"""Generated from the OpenAPI spec. Do not edit by hand."""


class _Endpoints:
    """One method per API endpoint; each returns the response `data`."""

    def collection_videos(self, collection_id, cursor=None, format=None):
        """List the videos inside a TikTok collection (one raw page per call, cursor-paginated).

        :param collection_id: Collection id (from /collections).
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param format: Omit for full raw objects (default). Use `clean` for a trimmed subset (id, desc, urls, music, stats).
        """
        return self._get('collection_videos', collection_id=collection_id, cursor=cursor, format=format)

    def collections(self, username, cursor=None, format=None):
        """List a user's TikTok collections (cursor-paginated).

        :param username: TikTok username, @handle, or profile URL.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param format: Omit for raw objects (default). Use `clean` for a trimmed subset (id, name, video_count, cover).
        """
        return self._get('collections', username=username, cursor=cursor, format=format)

    def comment_replies(self, video, comment_id, cursor=None, format=None):
        """All replies under one comment (one raw page per call, cursor-paginated).

        :param video: Video id, or any TikTok video/photo URL (incl. short vt./vm. links).
        :param comment_id: The comment's id (`cid` in raw /comments, `comment_id` in clean).
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response.
        :param format: Omit for the raw reply objects (default). `clean` for a trimmed subset.
        """
        return self._get('comment_replies', video=video, comment_id=comment_id, cursor=cursor, format=format)

    def comments(self, video, filter=None, cursor=None, format=None):
        """Fetch the comments on a video (id or URL).

        :param video: Video id, or any TikTok video/photo URL (incl. short vt./vm. links).
        :param filter: `top` (default, most relevant), `newest` (most recent first), `creator` (only the video author's comments), or `images` (comments that include images).
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param format: Omit for the full raw objects (default). Use `clean` for a trimmed subset (comment, user, likes, replies, …).
        """
        return self._get('comments', video=video, filter=filter, cursor=cursor, format=format)

    def hashtag_info(self, name=None, id=None, format=None):
        """Details of a hashtag - total views, number of videos, id and share link.

        :param name: Hashtag name, with or without #. Required unless `id` is given.
        :param id: Hashtag id (e.g. `hashtag_id` from /search_hashtags). Used instead of `name` when given.
        :param format: Omit for the raw `ch_info` object (default). `clean` for a trimmed subset.
        """
        return self._get('hashtag_info', name=name, id=id, format=format)

    def hashtag_videos(self, name=None, id=None, cursor=None, format=None):
        """Videos posted under a hashtag (one page per call, cursor-paginated).

        :param name: Hashtag name, with or without #. Required unless `id` is given.
        :param id: Hashtag id - skips the name lookup, so it's faster.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response.
        :param format: Omit for raw video objects (default). `clean` for a trimmed subset.
        """
        return self._get('hashtag_videos', name=name, id=id, cursor=cursor, format=format)

    def highlights(self, username, format=None):
        """Get a user's highlights - all collections and the stories inside each.

        :param username: TikTok username, @handle, or profile URL.
        :param format: Omit for the full raw story objects (default). Use `clean` for a trimmed subset (urls, cover, music, stats).
        """
        return self._get('highlights', username=username, format=format)

    def mix(self, mix_id, cursor=None, format=None):
        """Mix (creator playlist) details + the videos in it (one raw page per call, cursor-paginated).

        :param mix_id: TikTok mix id (as used in /@user/playlist/<name>-<mix_id>).
        :param cursor: Video page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param format: Omit for raw objects (default). Use `clean` for a trimmed mix + trimmed video objects.
        """
        return self._get('mix', mix_id=mix_id, cursor=cursor, format=format)

    def music(self, id, cursor=None, format=None):
        """Sound/music details + the videos that use it (one raw page per call, cursor-paginated).

        :param id: TikTok sound/music id (e.g. from a video's music object).
        :param cursor: Video page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param format: Omit for raw objects (default). Use `clean` for a trimmed sound subset + trimmed video objects.
        """
        return self._get('music', id=id, cursor=cursor, format=format)

    def posts(self, username, cursor=None, format=None):
        """List the videos a user has posted (one raw page per call, cursor-paginated).

        :param username: TikTok username, @handle, or profile URL.
        :param cursor: Opaque page cursor. Omit (or 0) for the first page; always pass back the `next_cursor` from the previous response as-is - it can be a number or a `c:<ms>` value.
        :param format: Omit for the full raw objects (default). Use `clean` for a trimmed subset (id, desc, urls, music, stats).
        """
        return self._get('posts', username=username, cursor=cursor, format=format)

    def reposts(self, username, cursor=None, with_repost_date=None, format=None):
        """List the videos a user has reposted (one raw page per call, cursor-paginated).

        :param username: TikTok username, @handle, or profile URL.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param with_repost_date: Set to 1 to also return `repost_date` (unix) per item - the moment the user reposted it, which the plain list does not carry. Costs one extra upstream call per page; items TikTok has no record for come back without the field.
        :param format: Omit for the full raw objects (default). Use `clean` for a trimmed subset (id, desc, urls, author, stats).
        """
        return self._get('reposts', username=username, cursor=cursor, with_repost_date=with_repost_date, format=format)

    def stories(self, username, cursor=None, format=None):
        """Fetch a user's active stories.

        :param username: TikTok username, @handle, or profile URL.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param format: Omit for the full raw objects (default). Use `clean` for a trimmed subset (media url, cover, stats, music, …).
        """
        return self._get('stories', username=username, cursor=cursor, format=format)

    def video_download(self, video):
        """Get a video's download URLs per quality (including the original file) by id or URL.

        :param video: Video id, or any TikTok video/photo URL (short links OK).
        """
        return self._get('video_download', video=video)

    def video_info(self, video, format=None):
        """Full info for a video by id or URL (raw object, or clean subset).

        :param video: Video id, or any TikTok video/photo URL (short links OK).
        :param format: Omit for the full raw `aweme_detail` (default). Use `clean` for a trimmed subset (desc, author, stats, music, hashtags, and country signals).
        """
        return self._get('video_info', video=video, format=format)

    def video_status(self, videos):
        """Check up to 40 videos in one call - is each still available (not deleted/removed)?

        :param videos: Comma-separated video ids or TikTok video URLs (max 40).
        """
        return self._get('video_status', videos=videos)

    def last_live(self, username):
        """Get a user's most recent live room by username - live now OR already ended - with its stats, duration, and top_fans (top

        :param username: TikTok username, @handle, or profile URL.
        """
        return self._get('last_live', username=username)

    def live(self, username=None, room_id=None):
        """Check if a user is live and get the stream URLs (HLS + FLV) per quality.

        :param username: TikTok username, @handle, or profile URL. (Use this OR room_id.)
        :param room_id: TikTok live room id (e.g. from /room_id). (Use this OR username.)
        """
        return self._get('live', username=username, room_id=room_id)

    def live_audience(self, room_id, anchor_id=None, format=None):
        """Top viewers currently in a live stream (the online-audience ranking, by contribution).

        :param room_id: TikTok live room id (get one from /room_id by username).
        :param anchor_id: The streamer's user id (improves accuracy; optional).
        :param format: Omit for the raw ranks (default). Use `clean` for a trimmed top-viewers list (rank, username, score, followers).
        """
        return self._get('live_audience', room_id=room_id, anchor_id=anchor_id, format=format)

    def live_chat(self, room_id, cursor=None):
        """Live chat & events of a LIVE room (comments, gifts, joins, likes).

        :param room_id: TikTok live room id (get one from /room_id by username).
        :param cursor: Omit (or 0) for the latest batch; pass the previous response's `next_cursor` to get newer events. Poll every ~1-2s to follow the chat live.
        """
        return self._get('live_chat', room_id=room_id, cursor=cursor)

    def live_gifts(self, room_id, cursor=None):
        """Gifts being sent in a LIVE room right now (sender, gift name, coins, combo).

        :param room_id: TikTok live room id (get one from /room_id by username).
        :param cursor: Omit (or 0) for the latest batch; pass the previous response's `next_cursor` for newer gifts. Poll every ~1-2s.
        """
        return self._get('live_gifts', room_id=room_id, cursor=cursor)

    def live_stats(self, username=None, user_id=None, history_limit=None):
        """A creator's live-centre stats: live status, fans club and gifts, and the full broadcast history with per-stream likes an

        :param username: TikTok username, @handle, or profile URL. (Use this OR user_id.)
        :param user_id: The numeric TikTok user id (from /profile → data.user.id). (Use this OR username.)
        :param history_limit: Return only the N most recent broadcasts. Defaults to all.
        """
        return self._get('live_stats', username=username, user_id=user_id, history_limit=history_limit)

    def room_id(self, username):
        """Get a user's live room_id by username (null if they're not live right now).

        :param username: TikTok username, @handle, or profile URL.
        """
        return self._get('room_id', username=username)

    def analytics(self, username=None, user_id=None, sec_uid=None, days=None, video=None, format=None):
        """Audience insights for a public creator account: follower breakdown by country, age and gender, an overview for a date ra

        :param username: The account's username. One of username / user_id / sec_uid is required.
        :param user_id: Numeric user id (instead of username).
        :param sec_uid: sec_uid (instead of username).
        :param days: Date window in days for the overview/time-series (default 7).
        :param video: A video id or URL - returns THAT video's analytics instead of the account's.
        :param format: Omit for the raw TikTok insight fields (default). `clean` for a tidy, flattened object.
        """
        return self._get('analytics', username=username, user_id=user_id, sec_uid=sec_uid, days=days, video=video, format=format)

    def current_region(self, username=None, user_id=None, sec_uid=None):
        """Get an account's current region (country) by its numeric user id.

        :param username: TikTok username, @handle, or profile URL. One of username / user_id / sec_uid is required.
        :param user_id: Numeric TikTok user id (instead of username).
        :param sec_uid: sec_uid (instead of username).
        """
        return self._get('current_region', username=username, user_id=user_id, sec_uid=sec_uid)

    def followers(self, username, cursor=None, format=None):
        """List an account's followers.

        :param username: TikTok username, @handle, or profile URL.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param format: Omit for the full raw objects (default). Use `clean` for a trimmed smart subset of each account.
        """
        return self._get('followers', username=username, cursor=cursor, format=format)

    def following(self, username, cursor=None, format=None):
        """List the accounts a user follows.

        :param username: TikTok username, @handle, or profile URL.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response for the next.
        :param format: Omit for the full raw objects (default). Use `clean` for a trimmed smart subset of each account.
        """
        return self._get('following', username=username, cursor=cursor, format=format)

    def profile(self, username=None, sec_uid=None, user_id=None, format=None):
        """Fetch a user's profile by username.

        :param username: TikTok username, @handle, or profile URL. (Provide one of username / sec_uid / user_id.)
        :param sec_uid: The account's secUid (alternative to username).
        :param user_id: The account's numeric user id (alternative to username).
        :param format: Omit for the full raw object (default). Use `clean` for a trimmed smart subset (name, country, stats, …).
        """
        return self._get('profile', username=username, sec_uid=sec_uid, user_id=user_id, format=format)

    def related_searches(self, video, query=None, format=None):
        """Related search terms suggested under a video ("others searched for").

        :param video: Video id, or any TikTok video/photo URL (incl. short vt./vm. links).
        :param query: Optional recent search to steer the words toward (without it they lean to what's trending).
        :param format: Omit for the raw word objects (default). `clean` for a plain list of words.
        """
        return self._get('related_searches', video=video, query=query, format=format)

    def search_hashtags(self, query, cursor=None, format=None):
        """Search hashtags (one page per call, cursor-paginated).

        :param query: What to search for.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response.
        :param format: Omit for raw challenge objects (default). `clean` for a trimmed subset (name, views, posts, description).
        """
        return self._get('search_hashtags', query=query, cursor=cursor, format=format)

    def search_music(self, query, cursor=None, format=None):
        """Search sounds/music (one page per call, cursor-paginated).

        :param query: What to search for.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response.
        :param format: Omit for raw music objects (default). `clean` for a trimmed subset (music_id, title, author, duration, user_count, play_url…).
        """
        return self._get('search_music', query=query, cursor=cursor, format=format)

    def search_photos(self, query, cursor=None, format=None):
        """Search photo/slideshow posts (one page per call, cursor-paginated).

        :param query: What to search for.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response.
        :param format: Omit for raw photo objects (default). `clean` for a trimmed subset (id, desc, images, author, stats).
        """
        return self._get('search_photos', query=query, cursor=cursor, format=format)

    def search_places(self, query, country=None, cursor=None, format=None):
        """Search places/POIs (venues, landmarks, restaurants).

        :param query: Place name or keyword.
        :param country: ISO-2 country code that localizes the results (e.g. US, SA, AE, GB, EG). Default US. This is what decides which country's places come back - not your location or the keyword.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response.
        :param format: Omit for raw POI objects (default). `clean` for a trimmed subset (name, address, country, lat/lng, video_count, rating).
        """
        return self._get('search_places', query=query, country=country, cursor=cursor, format=format)

    def search_suggest(self, query, format=None):
        """Search autocomplete - the suggestions shown while you type.

        :param query: The (partial) text typed so far.
        :param format: Omit for the raw suggestion objects (default). `clean` for a plain list of suggestion strings.
        """
        return self._get('search_suggest', query=query, format=format)

    def search_users(self, query, followers=None, verified=None, match=None, cursor=None, format=None):
        """Search users/accounts (one page per call, cursor-paginated).

        :param query: What to search for.
        :param followers: Only accounts with this many followers: `0-1k`, `1k-10k`, `10k-100k`, or `100k+`.
        :param verified: `true` to return only verified accounts.
        :param match: `username` to match the query against usernames (not display names).
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response. Keep the same filters when paging.
        :param format: Omit for raw account objects (default). `clean` for a trimmed subset (username, nickname, followers, verified, avatar).
        """
        return self._get('search_users', query=query, followers=followers, verified=verified, match=match, cursor=cursor, format=format)

    def search_videos(self, query, date=None, sort=None, cursor=None, format=None):
        """Search videos (one page per call, cursor-paginated).

        :param query: What to search for.
        :param date: Only videos posted within: `day`, `week`, `month`, `3months`, `6months`. Omit for all time.
        :param sort: `relevance` (default), `likes` (most liked first), or `newest` (latest first). Combines with `date`.
        :param cursor: Page cursor. Omit (or 0) for the first page; pass the `next_cursor` from the previous response. Keep the same filters when paging.
        :param format: Omit for raw video objects (default). `clean` for a trimmed subset (id, desc, stats, music, urls).
        """
        return self._get('search_videos', query=query, date=date, sort=sort, cursor=cursor, format=format)

    def trending_searches(self, region=None, count=None):
        """TikTok's rising search keywords for a region (what is being searched now).

        :param region: ISO-2 country code (default US).
        :param count: How many keywords to return (1-50, default 15).
        """
        return self._get('trending_searches', region=region, count=count)

    def resolve_url(self, url):
        """Expand a TikTok share/short link and extract the user, video, and share info.

        :param url: A TikTok share/short link (vt.tiktok.com, vm.tiktok.com, or /t/…).
        """
        return self._get('resolve_url', url=url)

    def usage(self):
        """Check your own key status: plan, remaining quota, and expiry.
        """
        return self._get('usage')
