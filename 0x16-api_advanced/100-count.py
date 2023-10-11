#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles """

import json
import requests


def count_words(subreddit, word_list, params=None):
    """
    function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited
    by spaces. Javascript should count as javascript, but java should not).
    """
    if params is None:
        params = {}

    base_url = "https://www.reddit.com/"
    user_url = f"{base_url}r/{subreddit}/hot.json"

    user_agent = {"User-Agent": "Python/requests"}

    response = requests.get(user_url, headers=user_agent, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        response_data = response.json()
        children = response_data.get("data", {}).get("children", [])

        word_count = {word: 0 for word in word_list}

        for article in children:
            title = article.get("data", {}).get("title", "")
            title_words = [word.strip('.!_') for word in title.lower().split()]
            for word in word_list:
                if word.lower() in title_words:
                    word_count[word] += title_words.count(word.lower())

        after = response_data.get("data", {}).get("after")
        if after:
            params["after"] = after
            count_words(subreddit, word_list, params)
        else:
            # Sort and print the results
            sorted_counts = sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word.lower()}: {count}")
    else:
        return
