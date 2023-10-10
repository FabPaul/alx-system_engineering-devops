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
    base_url = "https://www.reddit.com/"
    user_url = f"{base_url}/r/{subreddit}.hot.json"

    user_agent = {"User-Agent": "Python/requests"}

    response = requests.get(user_url, headers=user_agent, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
        hot_articles = response.get("data").get("children")

        word_count = collections.defaultdict(int)

        for article in articles:
            titles = children[i].get("data").get("title")
            words = lower().split()

            for word in words:
                if word in word_list:
                    word_count[word] += 1

        sorted_word_wount = dict(sorted(word_count.items,
                                 key=lambda x: x[0].lower()))
        return sorted_word_count
    else:
        return None
