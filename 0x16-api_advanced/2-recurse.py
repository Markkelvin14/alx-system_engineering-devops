#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user = {"User-Agent": "Markkelvin"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=user, params=params,
                            allow_redirects=False).json()

    results = response.get('data')
    after = results.get('after')
    count += results.get('dist')
    try:
        for res in results.get('children'):
            hot_list.append(res.get('data').get('title'))
    except Exception:
        return None

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
