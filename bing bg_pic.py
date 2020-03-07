import requests
from bs4 import BeautifulSoup

rr = requests.get('https://cn.bing.com/')
soup1 = BeautifulSoup(rr.text,'html.parser')
print(soup1)
tag_bg = soup1.find('div',id='bgDiv')#.find('div')
print(tag_bg)
part_url = (tag_bg['data-ultra-definition-src'].split('&'))[0]
pic = 'http://cn.bing.com'+part_url
print(pic)
