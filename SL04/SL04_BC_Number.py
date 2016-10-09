# -*- coding: utf-8 -*-

import json
import urllib2

def BC_num(num):
    # num = str(num)
    url = 'http://apis.baidu.com/datatiny/cardinfo/cardinfo?cardnum=' + num
    req = urllib2.Request(url)
    req.add_header('apikey','93a49a93791520c87a3ba7c7b04c6e9c')
    resp = urllib2.urlopen(req)
    data = json.loads(resp.read().decode("utf-8")).get('data')

    if data:
        print '卡号位数：',data.get('cardlength')
        print '银行名称：',data.get('bankname')
        print '卡的名字：',data.get('cardname')
        print '卡的类型：',data.get('cardtype')
        print '卡bin号：',data.get('cardprefixnum')
        print '银行代码：',data.get('banknum')

BC_num('DE34100700240045367000')