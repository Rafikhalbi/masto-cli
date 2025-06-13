from . import http_client, login
import json

def get_timeline() -> dict:
    """ get home time line """
    url = "https://mastodon.social/api/v1/timelines/home"
    response = http_client.rq_get(
        url= url, headers= login
    )
    return (json.loads(response.text))

def get_post_info(post_id: str) -> dict:
    """ get post information """
    url = 'https://mastodon.social/api/v1/statuses/{post_id}/context'
    response = http_client.rq_get(
        url= url, headers= login
    )
    return (json.loads(response.text))