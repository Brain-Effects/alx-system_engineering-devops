#!/usr/bin/python3
"""
Module to recursively query Reddit API for titles of all hot
articles of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    """
    headers = {'User-Agent': 'Python: subreddit.recurse: v1.0 (
            by / u/yourusername)'}
    url = f"https: // www.reddit.com/r/{
            subreddit}/hot.json?limit = 100 & after = {after}"

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    after = data.get('after')
    posts = data.get('children', [])

    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
