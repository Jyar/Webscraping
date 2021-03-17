from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('p')
    course_cards = soup.find_all('div',class_='card')
    for course_card in course_cards:
        print(course_card.h4)