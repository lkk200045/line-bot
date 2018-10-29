import requests #引入函式庫
from bs4 import BeautifulSoup
import re
url = 'https://tw.stock.yahoo.com/d/i/rank.php?t=vol&e=tse'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('td', re.compile('name'))
print(dcard_title)
if dcard_title =='國泰金':
	print(hello)
	low = soup.find_all('td', re.compile('low'))
	print(low)
