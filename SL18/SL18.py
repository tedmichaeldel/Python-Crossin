# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib


def picture(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    # 找到含有所有view_img_link的a标签
    pic_link_list = soup.find_all('a','view_img_link')
    pic_link = []
    for i in pic_link_list:
        pic_link.append(i.get('href'))
    # for j in pic_link:
    #   print j
    # 这个文件路径千万要加/,表示放到这个文件夹里面
    path_dir = 'Jandan_pic/'
    for link in pic_link:
        pic = urllib.urlopen(link).read()
        filename = link.split('/')[-1]
        print filename
        with open(path_dir + filename,'wb') as fh:
            fh.write(pic)


url = raw_input('输入jandan网址：')
picture(url)
