#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user = {"User-Agent": "Markkelvin"}
    response = requests.get(url, headers=user, allow_redirects=False).json()
    try:
        return response.get('data').get('subscribers')
    except Exception:
        return 0
