from bs4 import BeautifulSoup
import requests
import time

def find_headlines():
    html_text = requests.get('https://www.businesswire.com/portal/site/home/news/').text
    soup = BeautifulSoup(html_text, 'lxml')
    links = soup.find_all('a', class_ = 'bwTitleLink')
    print(links[0]['href'])
    headlines = soup.find_all('span', itemprop = 'headline')
    for idx,headline in enumerate(headlines):
        if 'filteredText' not in headline:
            print('headline#'+ str(idx) + ' ' + headline.string.encode('utf-8'))

if __name__ == '__main__':
    while True:
        # find_headlines()
        time_wait = 10
        print(f"hello {time_wait}")
        print('waiting ' + str(time_wait) + ' seconds...')
        time.sleep(time_wait)
