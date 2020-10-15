# -*- coding:utf-8 -*-
# _author_:wuzhonghui
# 2020/10/14

import requests, threading

urls = ['http://mirrors.163.com/centos/6/isos/x86_64/README.txt',
        'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt']

# for url in urls:
#     r = requests.get(url)
#     newText = r.text
#     with open('mergeTxt', 'w', encoding='utf8') as f:
#         f.write(newText)

lock = threading.Lock()
def readText(url):
    for i in url:
        r = requests.get(i)
        newText = r.text
        with open('mergeTxt', 'w', encoding='utf8') as f:
            f.write(newText)


readText(urls)





