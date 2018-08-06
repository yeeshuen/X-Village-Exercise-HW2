import requests
from bs4 import BeautifulSoup

from urllib.request import urlopen

url = 'https://www.ptt.cc/bbs/Boy-Girl/index.html'

for num in range(0,5):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_name = 'div.title a'
    articles = soup.select(tag_name)

    #其他page的文章
    paging = soup.select('div.btn-group-paging a')

    #看有多少Page
    print(paging)

    otherpage_url = paging[1]['href']
    next_url = 'https://www.ptt.cc'+otherpage_url
    url = next_url

    f = open('love04.txt', 'w',encoding='utf-8')
    for article in articles:
        print(article.text)
        f.write(article.text)

import jieba

ret = open("love1.txt", "r" , encoding="utf8").read()
seglist = jieba.cut(ret, cut_all=False)

import json
hash = {}
for item in seglist: 
    print(item)
    if item in hash:
        hash[item] += 1
    else:
        hash[item] = 1
json.dump(hash,open("count.json","w"))

fd = open("count.csv","w")
fd.write("word,count\n")
for k in hash:
    fd.write("%s,%d\n"%(k,hash[k]))














#container = soup.select('.r-ent')
#for each_item in container:
  #   print ("日期："+each_item.select('div.date')[0].text, "作者："+each_item.select('div.author')[0].text)
  #   print (each_item.select('div.title')[0].text)

#with open('movie_message.txt','w') as f:
   # for article in articles:
    #    #去除掉冒號和左右的空白
    #    messages = article.find('span','f3 push-content').getText().replace(':','').strip()
    #    print(messages)
   #     f.write(messages + "\n")