from bs4 import BeautifulSoup
import lxml

with open('base.html', 'r') as file:

    body = file.read()


# Get entire HTML.
soup = BeautifulSoup(body, 'lxml')
# print(soup.prettify())


# Get the title.
title = soup.title
# print(title)
# print(title.name)
# print(title.getText())


# Get the script tag.
body = soup.body
# print(body)
# print(body.name)
print(body.getText())
