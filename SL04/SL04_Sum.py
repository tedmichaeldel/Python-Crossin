# -*- coding: utf-8 -*-

import json
import urllib2


def ID(IDNumber):
    #　IDNumber = str(IDNumber)
    url = 'http://apis.baidu.com/apistore/idservice/id?id=' + IDNumber
    req = urllib2.Request(url)
    req.add_header('apikey', '93a49a93791520c87a3ba7c7b04c6e9c')
    resp = urllib2.urlopen(req)
    content = resp.read()
    content = content.decode("utf-8")
    data = json.loads(content).get('retData')
    print type(content)

    if data:
        if data.get('sex') == 'M':
            print '性别： 男'
        else:
            print '性别： 女'
        print '生日：', data.get('birthday')
        print '住址：', data.get('address')


def BC_num(num):
    # num = str(num)
    url = 'http://apis.baidu.com/datatiny/cardinfo/cardinfo?cardnum=' + num
    req = urllib2.Request(url)
    req.add_header('apikey', '93a49a93791520c87a3ba7c7b04c6e9c')
    resp = urllib2.urlopen(req)
    data = json.loads(resp.read().decode("utf-8")).get('data')

    if data:
        print '卡号位数：', data.get('cardlength')
        print '银行名称：', data.get('bankname')
        print '卡的名字：', data.get('cardname')
        print '卡的类型：', data.get('cardtype')
        print '卡bin号：', data.get('cardprefixnum')
        print '银行代码：', data.get('banknum')

id1 = raw_input('请输入身份证号：')
ID(id1)
bc_num = raw_input('请输入银行卡号：')
BC_num(bc_num)

