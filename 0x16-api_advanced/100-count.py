#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles """

import json
import requests


def count_words(subreddit, word_list, params={}):
    """
    function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited
    by spaces. Javascript should count as javascript, but java should not).
    """
    word_count = {word: 0 for word in word_list}
    total_words = len(word_count)
    limits = {}

    base_url = "https://www.reddit.com/"
    user_url = f"{base_url}/r/{subreddit}.hot.json"

    user_agent = {"User-Agent": "Python/requests"}

    response = requests.get(user_url, headers=user_agent, params=params,
                            allow_redirects=False)
    title = []

    if response.status_code == 200:
        response = response.json()
        hot_articles = response.get("data").get("children")

        for article in range(len(children)):
            titles = children[article].get("data").get("title").split()
            print(f"title:{titles}")
            after = response.get("data").get("after")

        if not after:
            return None
        else:
            limit = {"after": after, "a": a}
            count_words(subreddit, word_list, limit)
            return None
    else:
        return None
