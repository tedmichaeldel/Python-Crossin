# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname=101090101'

req = urllib2.Request(url)
req.add_header('apikey','93a49a93791520c87a3ba7c7b04c6e9c')

resp = urllib2.urlopen(req)
content = resp.read()
data = json.loads(content)
# list1 = content.get(retData)
# print type(content)
if data:
    print data.get('retData')

