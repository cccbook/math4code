import requests
import urllib.parse
import csv
import os
from bs4 import BeautifulSoup


EZPRICE_URL = 'https://ezprice.com.tw'
CSV_FILE_NAME = 'ezprice.csv'


def get_web_content(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Invalid url: ' + resp.url)
        return None
    else:
        return resp.text


def get_price_info(query, page):
    encoded_query = urllib.parse.quote(query)
    doms = list()
    for page in range(1, page + 1):
        url = EZPRICE_URL + '/s/%s/price/?q=%s&p=%s' % (encoded_query, encoded_query, str(page))
        result_page = get_web_content(url)
        doms.append(BeautifulSoup(result_page, 'html5lib'))
    return doms


def extract_results(dom):
    items = list()
    for div in dom.find_all('div', 'search-rst clearfix'):
        item = list()
        item.append(div.h4.a['title'])
        item.append(div.find(itemprop='price')['content'])
        if div.find('span', 'platform-name'):
            item.append(div.find('span', 'platform-name').text.strip())
        else:
            item.append('N/A')
        items.append(item)
    return items, len(items)


def show_results(items):
    for item in items:
        print(item)


def write_to_csv_file(is_first_page, items):
    with open(CSV_FILE_NAME, 'a', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        if is_first_page:
            writer.writerow(('Item', 'Price', 'Store'))
        for item in items:
            writer.writerow((column for column in item))


def read_from_csv_file():
    print('\nRead from csv file: ' + CSV_FILE_NAME)
    with open(CSV_FILE_NAME, 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['Item'], row['Price'], row['Store'])


def main():
    query = '吉胖喵'
    page = 5
    doms = get_price_info(query, page)
    is_first_page = True
    total_item_count = 0
    for dom in doms:
        items, count = extract_results(dom)
        total_item_count += count
        show_results(items)
        write_to_csv_file(is_first_page, items)
        is_first_page = False
    print('There are %s items in %d page(s).' % (total_item_count, page))
    read_from_csv_file()
    # Uncomment this if you don't want to keep the data in csv file.
    # os.remove(CSV_FILE_NAME)


if __name__ == '__main__':
    main()