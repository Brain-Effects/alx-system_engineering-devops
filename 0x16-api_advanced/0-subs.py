#!/usr/bin/python3
"""
Module to query the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
