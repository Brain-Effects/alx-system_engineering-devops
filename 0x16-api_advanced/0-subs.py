#!/usr/bin/python3
"""
Module to query the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a
    given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python: subreddit.subscriber.counter: v1.0\
            (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response JSON data: {data}")
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0
