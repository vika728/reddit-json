import requests

import json

def get_data(url):
    response = requests.get(url, headers= {'User-agent': 'your bot 0.1'})
    python_object = json.loads(response.text)
    news = python_object['data']['children']
    data = []
    number = 1
    for new in news:
        new_dictionary = {
                f'News No. {number}': {
                    'title': new['data']['title'],
                    'created': new['data']['created'],
                    'author': new['data']['author']
                }
        }
        number += 1
        data.append(new_dictionary)
    return data

def write_to_json(data):
    with open('RedditNews.json', 'w') as json_file:
        json.dump(data, json_file, indent = 4)


def main(url):
    data = get_data(url)
    write_to_json(data)
    print(data)

main('https://www.reddit.com/r/entertainment/.json')