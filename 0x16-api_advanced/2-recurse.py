#!/usr/bin/python3
""" Queries the reddit api and returns a list """

import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None.
    """
    base_url = "https://www.reddit.com/"
    user_url = f"{base_url}/r/{subreddit}/hot.json"

    user_agent = {"User-Agent": "Python/requests"}

    limits = {"after": after}

    response = requests.get(user_url, headers=user_agent, params=limits,
                            allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
        articles = response.get("data").get("children")
        after_data = response.get("data").get("after")

        for article in articles:
            hot_list.append(article.get("data").get("title"))

        if not after:
            recurse(subreddit, hot_list, after)

        return hot_list

    return None
