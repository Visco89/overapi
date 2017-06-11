from lxml import html
import requests

from div_costant import BASE_URL

def base_tree(user):
    page = requests.get(BASE_URL + user)
    page.raise_for_status()
    return html.fromstring(page.content)

if __name__ == '__main__':
    exit()