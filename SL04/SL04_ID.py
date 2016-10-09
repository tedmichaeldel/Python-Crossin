# -*- coding: utf-8 -*-

import json
import urllib2

def ID(IDNumber):
    url = 'http://apis.baidu.com/apistore/idservice/id?id=' + IDNumber
    req = urllib2.Request(url)
    req.add_header('apikey','93a49a93791520c87a3ba7c7b04c6e9c')
    resp = urllib2.urlopen(req)
    content = resp.read()
    content = content.decode("utf-8")
    data = json.loads(content).get('retData')
    print type(content)

    if data:
        if data.get('sex') is 'M':
            print '性别： 男'
        else:
            print '性别： 女'
        print '生日：', data.get('birthday')
        print '住址：', data.get('address')
ID('130102199009051874')
