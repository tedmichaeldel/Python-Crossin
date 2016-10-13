# -*- coding: utf-8 -*-

import json
import urllib2

def currency(type_c):

    url = 'http://apis.baidu.com/apistore/currencyservice/' + type_c

    req = urllib2.Request(url)
    req.add_header('apikey','93a49a93791520c87a3ba7c7b04c6e9c')
    resp = urllib2.urlopen(req)
    content = resp.read()
    if content:
        print content
        return content

currency('RMB')