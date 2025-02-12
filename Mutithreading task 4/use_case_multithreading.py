'''
Real world example : MultiThreading for I/O bound tasks
Scenario web scarapping
Web scrapping often involves making numerous network requests to fetch web page.
these task are I/O bound because they spend a lot of time 
waiting for response from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fethced concurrenly.


--
concurrently all the url is fetched.
'''

'''
https://celestialsys.com/
https://celestialsys.com/aboutus/security-accreditations/
https://celestialsys.com/case-studies/
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://celestialsys.com/',
'https://celestialsys.com/aboutus/security-accreditations/',
'https://celestialsys.com/case-studies/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched - {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target= fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")