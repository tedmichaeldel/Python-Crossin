# -*- coding: utf-8 -*-
# windows 下如果出现编码问题，将 utf-8 改为 cp936
# 抓煎蛋妹子图
import requests
import bs4

for page in range(2155, 2160):  # 设置想抓取的页数
    # 抓取页面内容，获取图片链接
    url = 'http://jandan.net/ooxx/page-%d' % page
    # 增加UA，避免抓取被禁
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    html = resp.text
    html = bs4.BeautifulSoup(html, "html.parser")  # 构S造bs对象
    link_pic_list = html.find_all('a', 'view_img_link')  # 获取所有class="view_img_link"的a标签
    # print link_pic_list
    url_pic_list = [l.get('href') for l in link_pic_list]  # 把其中的href属性取出
    # print url_pic_list

    path_dir = 'pics/'  # 存放地址，需事先创建好文件夹
    for url_pic in url_pic_list:
        # 抓取列表地址中的每一张图片，获取图片内容
        resp = requests.get(url_pic, headers=headers)
        pic = resp.content
        file_name = url_pic.split('/')[-1]  # 从url中截出图片文件名
        print file_name
        # 保存至本地文件中
        with open(path_dir + file_name, 'wb') as f:
            f.write(pic)

