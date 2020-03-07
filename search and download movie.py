#一键下载电影
import requests
from bs4 import BeautifulSoup
from urllib.request import quote

client_search = True
while client_search:
    search = input('请输入电影中文名称：')
    search_title = quote(search.encode('gbk'))
    url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+search_title
    print('搜索结果页面直达：'+url)
    r = requests.get(url)
    r.encoding = 'gbk'
    s = BeautifulSoup(r.text,'html.parser')
    info = s.find('div','co_content8').find('ul').find_all('b') #all search results
    if len(info)!=0:
        print('（共{}条搜索结果）'.format(len(info)))
        if len(info)>=10:
            print('注：搜索结果较多，请确认片名的完整性。')
            user_choice = input('重新搜索请输入0，按其他任意键继续：')
            if user_choice=='0':
                continue
            else:
                client_search = False
        else:
            break
    
    else:
        print('no movie')
        continue

for i in info:
    if info.index(i)>=3:
        break
    else:
        title = i.a.text
        link = 'https://www.ygdy8.com'+i.a['href']
        print('第{}条结果：'.format(info.index(i)+1))
        print(title)
        print('影片页面直达：'+link) 
        r = requests.get(link)
        r.encoding = 'gbk'
        s = BeautifulSoup(r.text,'html.parser')
        download_link = s.find('div',id='Zoom').table.a.text
        print(download_link)
        print()