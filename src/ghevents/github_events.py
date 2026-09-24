#!usr/bin/python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events():
    """Download data and create a dictionary"""
    data = requests.get(url).text
    dict = json.loads(data)
    return dict

def print_events(events, n=5):
    """Prints all of the events"""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    print(GHUSER)
    print(url)
    event = retrieve_events(url)
    print_events(event)

if __name__ == "__main__":
    main()
    
    

    