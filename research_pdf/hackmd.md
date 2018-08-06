


## 探討華文流行情歌歌詞與產生情感的關聯性
## Power of love songs: that trigger emotions. 

Author: 方瑜瑄 / Hung Yee Shuen

## Aim of this investigation
- Analyse if there's a relationship between preference of love songs and listeners' emotions. 
- Analyse if top hits' love songs have specific key words that can relate to the feelings of listeners. 

#### 探討問題
1）探討情歌歌詞與聽者的選擇是否有關聯。
2）探討熱門歌曲歌詞與聽者的情感是否有關聯。
-是不是歌詞裡有失戀者會想到的關鍵字會更觸動他們的心呢。

#### 研究題材
1）PTT 感情版 文章
2）KKBOX 熱門歌曲 2016-2018 TOP30
3）熱門歌手 - 林俊傑，周杰倫，等歌手熱門歌曲。

#### 研究方法
一，研究設計
 本研究採用的分析方式為
 1）PYTHON 爬蟲
 2）文字雲
 
 ------------------------------
 ## **探討情感關鍵字**
 
**1) PTT BOY-GIRL 板**
 
 在**探討情感關鍵字**，我們利用python爬蟲抓出PTT版中的感情版，再進行文字雲探討在文章中出現最多的關鍵字。
 
 
## Step1
用以下的code來執行分析PTT感情版上的文章
```python
#PTT 心情版爬蟲
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

    f = open('love1.txt', 'w',encoding='utf-8')
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
```

## Step2
以下code是分析PTT文章後，做出文字雲。
```python
#PTT 文字雲
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open('ptt_04.txt' ,"r" , encoding="utf8").read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(font_path="C:\Windows\Fonts\setofont.ttf").generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
```

### 截取2018/08/04 PTT BOY-GIRL 心情板 （67筆文章）

![](https://i.imgur.com/rUV5CxK.png)

![](https://i.imgur.com/nD7dZZK.png)

----------------------------------

## **探討情感關鍵字**
 
**2) DCARD**
 
 在**探討情感關鍵字**，我們利用python爬蟲抓出DCARD版中的感情版前30篇熱門文章，再進行文字雲探討在文章中出現最多的關鍵字。
 
```python 
import requests 
from bs4 import BeautifulSoup
import re
url = 'https://www.dcard.tw/f/relationship'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))
print('Dcard 感情版熱門前三十文章標題：')
for index, item in enumerate(dcard_title[:30]):
    print("{0:2d}. {1}".format(index + 1, item.text.strip()))
```
 
 ### Dcard 感情板前30篇熱門文章
 ![](https://i.imgur.com/T3uQKFs.png)

```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open('dcard_30.txt' ,"r" , encoding="utf8").read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(font_path="C:\Windows\Fonts\setofont.ttf").generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
```

### 截取2018/08/04 & 05 
### Dcard 感情版熱門文章關鍵字文字雲
![](https://i.imgur.com/p0xsgx5.png)

![](https://i.imgur.com/xb7nFJO.png)

--------------------------------
## **探討情歌歌詞與情感是否有相關**
 
**1）情歌歌詞**
 
 在**探討情歌歌詞的部分**，我們利用python爬蟲抓出KKBOX 2016-2018年的熱門歌曲歌單，再進行文字雲探討在歌詞中出現最多的關鍵字是否和情感（PTT,DCARD）中出現的字有相同。
 
* KKBOX 2016-2018年 熱門歌曲歌詞

我先把歌詞copy進txt file
##### [kkbox_top50.txt]
![](https://i.imgur.com/my9FtkH.png)

```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open('kkbox_top50.txt' ,"r" , encoding="utf8").read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(font_path="C:\Windows\Fonts\setofont.ttf").generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
```


![](https://i.imgur.com/uLdkIBR.png)

* JJ林俊傑 KKBOX 熱門歌曲歌詞

#### JJ_top30.txt

![](https://i.imgur.com/owXtKsk.png)

![](https://i.imgur.com/72HvGmT.png)

#### jay_top30.txt

![](https://i.imgur.com/1qnFcRs.png)

![](https://i.imgur.com/bJ3QKXN.png)







-----------------------------------------------------------------------
建立一個csv- list出全部關鍵字的數量
----------------------------------
```python
import jieba

#讀取熱門歌曲的熱門文字
ret = open("kkbox_top50.txt", "r" , encoding="utf8").read()
seglist = jieba.cut(ret, cut_all=False)

import json
hash = {}
for item in seglist: 
    print(item)
    if item in hash:
        hash[item] += 1
    else:
        hash[item] = 1
json.dump(hash,open("count_kkbox.json","w"))
print(hash)

fd = open("count_kkbox.csv","w")
fd.write("word,count\n")
for k in hash:
    fd.write("%s,%d\n"%(k,hash[k]))

```
#### 由於我的電腦編碼屬於外國系統，所以無法讀取以上的文章文字，csv檔出現錯誤亂碼。






## 結論：




### 過程發現的問題，
1） 由於我的電腦不在台灣本地購入，編碼上一直出現錯誤，無法讀取華文檔案，即使已經換了語言，下載了繁體中文的系統也無法。在這部分可能需要再嘗試。

2）因為讀不到中文字，所以我的系統上無法載入jieba，在文字處理中，斷字的部分目前屬於手動處理。


