#-*- coding:utf-8 -*-
import requests
import re
import csv
from pyquery import PyQuery as pq
import os

def get_file_magnet_link_test(id):  ##查找方式:PyQuery
    import re
    import requests
    from pyquery import PyQuery as pq
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    web = requests.get('https://m.zhongziso.com/list/' + id + '/1', headers=headers)
    doc = pq(web.text)
    a = doc('.down a')
    return a.attr('href')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

print("Number Geter By:rockstar99")
inputurl = input("Please enter URL here https://:")
filess = input("Please enter the path of file.Example:C:/aaa.csv:")
page = input("Please enter the number of pages to be grabbed:")

handleurl = re.search(re.compile('www.ff8.xyz/tag-vod-wd-\S+-p-',re.S),inputurl)

print("=========================================================================")
print("The number of movies:", 40*int(page),"\nThere are 40 movies on each page.")

#以下为翻页爬虫操作:
count = 0
while (count < int(page)):
    counts=int(count)+1
    web = requests.get('https://'+str(handleurl.group(0))+str(counts) +'.html', headers=headers)

    print('https://'+str(handleurl.group(0))+str(counts) +'.html')
    print("Catching the NO."+str(counts)+" page.")
    print("There are still",int(count)*40,"films left.")

    ID = re.findall(re.compile('<td>.*?<a href="\S*.html">(.*?)</a>', re.S), web.text)
    title = re.findall(re.compile('<td>.*?<a href="\S*.html" target="_blank">(.*?)</a>', re.S), web.text)

    zidian1 = dict(zip(ID, title))

    def get_file_magnet_link(id):  # 查找方式:正则表达式
        import re
        import requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        web = requests.get('https://m.zhongziso.com/list/' + id + '/1', headers=headers)
        a = re.search('(magnet:?[^\"]+)', web.text)
        return a.group(0)

    def get_file_magnet_link_test(id):  ##查找方式:PyQuery
        import re
        import requests
        from pyquery import PyQuery as pq
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        web = requests.get('https://m.zhongziso.com/list/' + id + '/1', headers=headers)
        doc = pq(web.text)
        a = doc('.down a')
        return a.attr('href')

    def putListCsv(file, list, list2):
        zidian = dict(zip(list, list2))
        with open(file, 'a+', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            listss = len(ID)
            i = 1
            for list, list2 in zidian.items():
                zidianss = len(zidian)
                list3 = get_file_magnet_link_test(list)
                print(list, ",", list2, ",", list3, file=csvfile)
                print("[" + str(i) + "/" + str(zidianss) + "]", list, ",", list2, ",", list3)
                i = i + 1

    putListCsv(filess, ID, title)
    count = count + 1

print("Finshed!")
