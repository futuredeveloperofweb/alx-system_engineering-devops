#!/usr/bin/python3
'''a function that queries the Reddit API and returns the number of
subscribers for a given subreddit'''
import requests
import sys


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                subscribers = data.get('subscribers', 0)
                return int(subscribers)
        else:
            return 0
    except Exception as e:
        return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(number_of_subscribers(sys.argv[1]))
    else:
        print("Usage: script.py <subreddit>")
