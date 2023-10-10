#!/usr/bin/python3
"""Function to query 10 hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """return 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user = {"User-Agent": "Marklevin"}
    params = {"limit": 10}
    response = requests.get(url, headers=user, params=params,
                           allow_redirects=False).json()
    try:
        for res in response.get('data').get('children'):
            print(res.get('data').get('title'))
    except Exception:
        print(None)
