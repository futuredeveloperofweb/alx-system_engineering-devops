#!/usr/bin/python3
'''a function that queries the Reddit API and returns the number of
subscribers for a given subreddit'''

import requests


def number_of_subscribers(subreddit):
    '''returns the number of subscribers for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
    return 0


if __name__ == '__main__':
    number_of_subscribers(argv[1])
