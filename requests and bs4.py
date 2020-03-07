# import requests
# from bs4 import BeautifulSoup

# for i in range(10):
#     url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
#     r = requests.get(url)
#     s = BeautifulSoup(r.text,'html.parser')
#     info = s.find_all('div','item')
#     for i in info:
#         with open('Top250 douban.txt','a') as t:
#             num = i.find('div','pic').em.text
#             title = i.find('div','info').a.text.replace('\n','')
#             rate = i.find('span','rating_num').text
#             t.write(num+' '+title+'\n')
#             t.write(' '*len(num)+' '+'rating: '+rate)
            
#             if i.find('p','quote')!=None:
#                 quote = i.find('p','quote').text.replace('\n','')
#                 t.write('\t\"'+quote+'\"\n')
#             else:
#                 t.write('\t-\n')
            
#             link = i.find('div','info').a['href']
#             t.write(' '*len(num)+' '+link+'\n\n')
    

#分别提取所有的序号/所有的电影名/所有的评分/所有的推荐语/所有的链接，然后再按顺序一一对应起来。

import requests
from bs4 import BeautifulSoup

for i in range(10):
    url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    r = requests.get(url)
    s = BeautifulSoup(r.text,'html.parser')
    info = s.find_all('div','item')
    for i in info:
        num = i.em.text
        title = i.find('div','hd').a.text.replace('\n','')
        rating = i.find('span','rating_num').text
        if i.find('p','quote')!=None:
            quote = i.find('span','inq').text
        else:
            quote = '-'
        url = i.find('div','hd').a['href']
        print(num+' '+title)
        print(' '*len(num)+' rating: '+rating,'  \"'+quote+'\"')
        print(' '*len(num),url,'\n')
