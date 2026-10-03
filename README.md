# omarthing

Python client for the [Omar-Thing TikTok API](https://dev.omar-thing.site): profiles, followers,
videos, comments, stories, hashtags, search and live data as plain Python methods.

```bash
pip install omarthing
```

You need an API key from https://dev.omar-thing.site. Pass it in, or set `OMARTHING_API_KEY`.

```python
from omarthing import Client

api = Client("YOUR_API_KEY")

profile = api.profile(username="tiktok", format="clean")
print(profile["nickname"], profile["followers"])

# paginated endpoints: feed next_cursor back in until has_more is False
cursor = None
while True:
    page = api.posts("tiktok", cursor=cursor, format="clean")
    for post in page["posts"]:
        print(post["id"], post["desc"][:60])
    if not page["has_more"]:
        break
    cursor = page["next_cursor"]
```

Every method returns the `data` part of the response. Required arguments come first, optional
ones are keyword arguments and are skipped when `None`.

## Errors

```python
from omarthing import Client, OmarThingError

try:
    Client("YOUR_API_KEY").profile(username="tiktok")
except OmarThingError as e:
    print(e.status_code, e.code, e.message, e.request_id)
```

429 and 502/503/504 are retried (`retries=2`, respects `Retry-After`). `api.usage()` shows your quota.

`Client(api_key=None, base_url=None, timeout=60, retries=2)`; `base_url` defaults to
https://dev.omar-thing.site (or `$OMARTHING_BASE_URL`).

## Methods

Parameters for each endpoint are documented at https://dev.omar-thing.site/docs.html
(OpenAPI spec: [omarthing-openapi](https://github.com/omar-thing/omarthing-openapi)).

**Content**

| Method (`*` = required) | What it does |
|---|---|
| `collection_videos(*collection_id, cursor, format)` | List the videos inside a TikTok collection (one raw page per call, cursor-paginated). |
| `collections(*username, cursor, format)` | List a user's TikTok collections (cursor-paginated). |
| `comment_replies(*video, *comment_id, cursor, format)` | All replies under one comment (one raw page per call, cursor-paginated). |
| `comments(*video, filter, cursor, format)` | Fetch the comments on a video (id or URL). |
| `hashtag_info(name, id, format)` | Details of a hashtag - total views, number of videos, id and share link. |
| `hashtag_videos(name, id, cursor, format)` | Videos posted under a hashtag (one page per call, cursor-paginated). |
| `highlights(*username, format)` | Get a user's highlights - all collections and the stories inside each. |
| `mix(*mix_id, cursor, format)` | Mix (creator playlist) details + the videos in it (one raw page per call, cursor-paginated). |
| `music(*id, cursor, format)` | Sound/music details + the videos that use it (one raw page per call, cursor-paginated). |
| `posts(*username, cursor, format)` | List the videos a user has posted (one raw page per call, cursor-paginated). |
| `reposts(*username, cursor, with_repost_date, format)` | List the videos a user has reposted (one raw page per call, cursor-paginated). |
| `stories(*username, cursor, format)` | Fetch a user's active stories. |
| `video_download(*video)` | Get a video's download URLs per quality (including the original file) by id or URL. |
| `video_info(*video, format)` | Full info for a video by id or URL (raw object, or clean subset). |
| `video_status(*videos)` | Check up to 40 videos in one call - is each still available (not deleted/removed)? |

**Live**

| Method (`*` = required) | What it does |
|---|---|
| `last_live(*username)` | Get a user's most recent live room by username - live now OR already ended - with its stats, duration, and top_fans (top |
| `live(username, room_id)` | Check if a user is live and get the stream URLs (HLS + FLV) per quality. |
| `live_audience(*room_id, anchor_id, format)` | Top viewers currently in a live stream (the online-audience ranking, by contribution). |
| `live_chat(*room_id, cursor)` | Live chat & events of a LIVE room (comments, gifts, joins, likes). |
| `live_gifts(*room_id, cursor)` | Gifts being sent in a LIVE room right now (sender, gift name, coins, combo). |
| `live_stats(username, user_id, history_limit)` | A creator's live-centre stats: live status, fans club and gifts, and the full broadcast history with per-stream likes an |
| `room_id(*username)` | Get a user's live room_id by username (null if they're not live right now). |

**Profiles & Users**

| Method (`*` = required) | What it does |
|---|---|
| `analytics(username, user_id, sec_uid, days, video, format)` | Audience insights for a public creator account: follower breakdown by country, age and gender, an overview for a date ra |
| `current_region(username, user_id, sec_uid)` | Get an account's current region (country) by its numeric user id. |
| `followers(*username, cursor, format)` | List an account's followers. |
| `following(*username, cursor, format)` | List the accounts a user follows. |
| `profile(username, sec_uid, user_id, format)` | Fetch a user's profile by username. |

**Search**

| Method (`*` = required) | What it does |
|---|---|
| `related_searches(*video, query, format)` | Related search terms suggested under a video ("others searched for"). |
| `search_hashtags(*query, cursor, format)` | Search hashtags (one page per call, cursor-paginated). |
| `search_music(*query, cursor, format)` | Search sounds/music (one page per call, cursor-paginated). |
| `search_photos(*query, cursor, format)` | Search photo/slideshow posts (one page per call, cursor-paginated). |
| `search_places(*query, country, cursor, format)` | Search places/POIs (venues, landmarks, restaurants). |
| `search_suggest(*query, format)` | Search autocomplete - the suggestions shown while you type. |
| `search_users(*query, followers, verified, match, cursor, format)` | Search users/accounts (one page per call, cursor-paginated). |
| `search_videos(*query, date, sort, cursor, format)` | Search videos (one page per call, cursor-paginated). |
| `trending_searches(region, count)` | TikTok's rising search keywords for a region (what is being searched now). |

**Utilities**

| Method (`*` = required) | What it does |
|---|---|
| `resolve_url(*url)` | Expand a TikTok share/short link and extract the user, video, and share info. |

**Your Key**

| Method (`*` = required) | What it does |
|---|---|
| `usage()` | Check your own key status: plan, remaining quota, and expiry. |


`live_chat` and `live_gifts` are polled: call them in a loop and pass the returned cursor back in
(see `live_chat_reader.py` in [tiktok-api-examples](https://github.com/omar-thing/tiktok-api-examples)).

## License

MIT. Unofficial: not affiliated with or endorsed by TikTok or ByteDance.
