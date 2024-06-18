#!/usr/bin/python3
"""
Module to recursively query Reddit API, parse titles of hot
articles, and print sorted count of keywords
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, hot_list=[], after="", count={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    headers = {'User-Agent': 'Python: subreddit.count_words: v1.0 (
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
        title = post.get('data', {}).get('title', "").lower()
        words = [word for word in title.split(
                 ) if word.strip('.,!?_') in word_list]
        hot_list.extend(words)

    if after is not None:
        return count_words(subreddit, word_list, hot_list, after, count)

    word_count = Counter(hot_list)
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, freq in sorted_words:
        print(f"{word}: {freq}")
