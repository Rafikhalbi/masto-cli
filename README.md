# masto_cli

`masto_cli` is a Python wrapper for interacting with the [Mastodon](https://mastodon.social) API.  
It simplifies authentication, posting statuses, retrieving user info, and interacting with the timeline — all from a Python script.

## Features

- Login via session cookies
- Get user ID, followers, followings
- Post statuses with media
- Like (favourite) posts
- Reply to posts
- View timeline

## Installation

```bash
pip install masto-cli
```

## Example Login
```python
from masto_cli import (
    login, auth
)
import json

# generete cookie
signIn = auth.get(login.get_cookie(email="email@email.com", password="password"))

# save cookie to login.json
json.dump(signIn, open("login.json", "w"))

```

## Example get user information  
```python
from masto_cli import get_id_info, get_username_info

# find user by username
user = get_username_info("Rafikhalbi")
print(user)

# or by id
user = get_id_info(1)
print(user)
```

## Example post text, image, video or music
```python
from masto_cli import Publish
```
```python
# text only
send = Publish(text="Test send status from python").status()
```

```python
# with file
media_path = ["iamge1.jpg", "image2.jpg", "image3.jpg"]
send = Publish(text="Test send status from python", media_path= media_path).status()
```

# Others

| Function                          | Description                        |
|----------------------------------|------------------------------------|
| `get_following(user_id)`        | Get user's following list          |
| `get_followers(user_id)`        | Get user's followers list          |
| `get_timeline()`                | Get home timeline                  |
| `Publish(text, media_path).status()`     | Post a status with optional media  |
| `Publish(text).reply(post_id)` | Reply to a specific post by post ID. |
| `favourite(post_id)`            | Like a post                        |
| `follow(user_id)`               | Follow a user                      |
| `unfollow(user_id)`             | Unfollow a user                    |
