from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.google.com/search?sxsrf=ALeKk00Dqk9-wp8IeCwY4yA4vKrVLndJyA%3A1614226191087&ei=DyM3YIDMBNWt5NoPoMmSCA&q=games+top+stock&oq=games+top+stock&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEAoQRhD6ATICCAAyBAgAEAoyBAgAEAoyAggAMgQIABAKMgQIABAKMgQIABAKMgIIADIECAAQCjoHCCMQsAMQJzoHCAAQsAMQQzoHCAAQRxCwAzoECCMQJzoNCAAQhwIQsQMQgwEQFDoFCAAQsQM6BAgAEEM6CAgAELEDEIMBOgoIABCxAxCDARBDOgcIABCxAxBDOgcIIxDqAhAnOgcIIxAnEJ0COg0ILhCxAxDHARCjAhBDOgcILhCxAxBDOggIABCxAxDJAzoFCAAQkgM6DAgjECcQnQIQRhD6AToHCAAQhwIQFDoKCAAQhwIQsQMQFDoICC4QxwEQrwE6DgguELEDEMcBEKMCEJMCOgcIABDJAxAKOgYIABAKEAM6BQgAEMkDOgIILlCHG1jfPmDwQGgDcAJ4AYAB8AKIAdgOkgEIMTcuMi4wLjGYAQCgAQGqAQdnd3Mtd2l6sAEKyAEKwAEB&sclient=gws-wiz&ved=0ahUKEwjAj9OVlYTvAhXVFlkFHaCkBAEQ4dUDCA0&uact=5').text.encode('utf-8')
# print('soup:' + html_text)

soup = BeautifulSoup(html_text, 'lxml')
search_results = soup.find_all('a', class_ = 'BVG0Nb')
for search_result in search_results:
    print(search_result.text)