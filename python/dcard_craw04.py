import requests #引入函式庫
from bs4 import BeautifulSoup
import re
url = 'https://www.dcard.tw/f/relationship'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))
print('Dcard 感情版熱門前三十文章標題：')
for index, item in enumerate(dcard_title[:50]):
    print("{0:1d}. {1}".format(index + 1, item.text.strip()))

