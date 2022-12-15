import requests
import re
from bs4 import BeautifulSoup


def main():
    dcard_topic_page = 'https://www.dcard.tw/f'
    resp = requests.get(dcard_topic_page)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # ^ means "start with"
    topic_entry_pattern = '^PostEntry_container_'
    topic_title_pattern = 'strong'
    find_top10_hot_topic_title(soup, topic_entry_pattern, topic_title_pattern)


def find_top10_hot_topic_title(soup, topic_entry_pattern, topic_title_pattern):
    top_ten_topic = soup.find_all('div', {'class': re.compile(topic_entry_pattern)})
    i = 1
    for topic in top_ten_topic[:10]:
        print(str(i) + ': ' + topic.find(topic_title_pattern).text)
        i += 1


if __name__ == '__main__':
    main()