import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
link = 'http://www.paudefogo.com.br'

driver.get('http://www.paudefogo.com.br')
print(driver.current_url)

site = driver.current_url

response = requests.get(site)

final_site = response.url

response = requests.get(final_site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if filename is None:
        continue
    with open('temp_images/'+filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative
            # if it is provide the base url which also happens
            # to be the site variable atm.
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)