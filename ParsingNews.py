import requests
from bs4 import BeautifulSoup

url = "https://us.cnn.com/asia"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

titleElement = soup.select_one("#asia-zone-1 > div.l-container > div > div:nth-child(1) > ul > li > article > div > div.cd__content > h3 > a > span.cd__headline-text.vid-left-enabled")
print(titleElement)