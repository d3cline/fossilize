## fossilize
Dynamic mastodon domain blocker

# Synopsis
There is a need for instance admins to safeguard from unsolicited messages,
exploit vectors, and content deemed inappropriate by their communities.
Mastodon needs a dynamic health metric similar to the X-SPAM score on email.
The metric can then be used to set automatic block rules based on the score.
This requires both domain level and user level metrics for dynamic blocking and muting.
A tool which sits outside of the mastodon code base and uses the API to interface with mastodon makes sense.
It can move at a faster pace from the internal code base, and it can benefit and track the entire fediverse.
Lists of peers are provided by Mastodon itself as well as projects like `poduptime`.
Domain information can be polled from RDAP, as well as email abuse APIs.
AI libraries like pytorch can provide content moderation assistance.

![description](https://raw.githubusercontent.com/d3cline/fossilize/main/concept.png)

# Tasks
- Build functions for obtaining the domain from mastodon and poduptime.
- Build functions for obtaining information from RDAP databases.
- Build functions for determining 'RDAP Score'
- Build functions to obtain user data from a given instance.
- Build functions to send user data into pytorch and perform some tasks such as emotion score.
  - EmoRoBERTa
- Determine how we want to store the data. Django, FastAPI, SQLite. (I know django really well, but I dont really feel its right for this)
  - Minio
- Determine how we set automatic tasks based on scores. 
- Determine how we want to notify the admin.
- Determine how user based scoring might work. 
- Use Mastodon.py to interface with mastodon API. 

## This code is experimental and in constant change. 
