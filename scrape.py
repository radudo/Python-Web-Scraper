import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
#Find All Tags from a bigger section
tags = soup.find_all('div', class_='tags')

for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    #Iterate Throug The Tags in the Div for each
    quoteTags = tags[i].find_all('a', class_='tag')
    #Display Iteration
    for quoteTag in quoteTags:
        print(quoteTag.text)
