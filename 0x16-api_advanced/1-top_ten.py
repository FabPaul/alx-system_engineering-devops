#!/usr/bin/python3
""" queries Reddit API and prints the titles """

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """

    base_url = "https://www.reddit.com/"
    user_url = f"{base_url}/r/{subreddit}/hot.json"

    user_agent = {"User-Agent": "Python/requests"}

    limits = {"limit": "10"}

    response = requests.get(user_url, headers=user_agent, params=limits,
                            allow_redirects=False)

    if response.status_code in [301, 302, 400, 404]:
        print("None")
    else:
        json_respn = response.json()

        if json_respn.get("data") and json_respn.get("data").get("children"):
            hot_posts = json_respn.get("data").get("children")

            for post in hot_posts:
                if post.get("data") and post.get("data").get("title"):
                    the_post = post.get("data").get("title")
                    print(the_post)
