import requests
import csv
from bs4 import BeautifulSoup
from random import randint
from time import sleep


file = open('phoneslist.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['მობილურის მოდელი' , 'ფასი'])

page_number = 1
while page_number <= 5:
    url = f'https://alta.ge/smartphones-page-{page_number}.html?sort_by=popularity&sort_order=desc'
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    phones = soup.find('div', class_='grid-list')
    all_phones = phones.find_all('div', class_='ty-column3')
    page_number+=1

    for phone in all_phones:
        name = phone.find('a', class_='product-title')
        price = phone.find('span', class_='ty-price-num')
        csv_obj.writerow([name.text , price.text])

sleep(randint(15,20))