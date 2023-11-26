from bs4 import BeautifulSoup
import requests
import random

def find_amt_page(anekother_url):
    page_first = requests.get(anekother_url)
    soup_first = BeautifulSoup(page_first.text, 'lxml')
    search_amt = soup_first.find('div', class_= 'list')
    search_amt = search_amt.find_all('a', class_= 'nav')
    amt = int(search_amt[4].text) # Под 5 элементом хранится количество страниц
    return amt

def find_anekdot():
    anekother_url = 'https://nekdo.ru/other/'

    amt_page = find_amt_page(anekother_url) # Количество страниц других анекдотов
    
    num_page = random.randint(1, amt_page) # Выбираем рандомную страницу
        
    page = requests.get(anekother_url + str(num_page) + '/') # Находим эту страницу
        
    soup = BeautifulSoup(page.text, 'lxml') # Выгружаем html код этой страницы
        
    search_anek_page = soup.find_all('div', class_='text') # Закидываем все анекдоты на сранице
        
    num_anek = random.randint(1, len(search_anek_page)) # Выбираем один рандомный анекдот
        
    anek = search_anek_page[num_anek - 1].text
 
    return anek
