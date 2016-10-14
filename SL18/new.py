# -*- coding: utf-8 -*-
import requests

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
    }
path_dir = 'pics/'
url_pic = 'http://ww2.sinaimg.cn/large/006Aqhvjjw1f8o0hzu8h3j30p011gq5d.jpg'
resp = requests.get(url_pic, headers=headers)
pic = resp.content
file_name = url_pic.split('/')[-1]  # 从url中截出图片文件名
print file_name
# 保存至本地文件中
with open(path_dir + file_name, 'w') as f:
    f.write(pic)