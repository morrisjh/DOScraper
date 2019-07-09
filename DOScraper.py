import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://digitalorientalist.com/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='texts')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Date', 'Category', 'Content', 'Link']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find('a')['title'][13:100] 
        date = post.find('time')['datetime'][0:10]
        category = post.find(class_='categories').get_text().replace('\n', '')
        content = post.find('p').get_text().replace('\n', '')
        link = post.find('a')['href']
        csv_writer.writerow([title, date, category, content, link,])