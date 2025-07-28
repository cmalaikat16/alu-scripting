#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    print(f"Status Code: {response.status_code}")  # Debugging line
    
    if response.status_code != 200:
        print(None)
        if response.status_code == 404:
            print("Subreddit not found")
        elif response.status_code == 403:
            print("Access forbidden")
        else:
            print("An error occurred")
        return
    
    try:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print("Error parsing response")
