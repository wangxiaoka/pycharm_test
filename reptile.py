# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib

#request = urllib.request.Request("http://www.baidu.com")
#response = urllib.request.urlopen("http://www.baidu.com")
#response = urllib.request.urlopen(request)
#print (response.read())

values = {"username":"wang531882703","password":"ka.1416.."}
data = urllib.parse.urlencode(values).encode(encoding='UTF-8')
url = "https://mail.qq.com/cgi-bin/loginpage"
request = urllib.request.Request(url, data)
response = urllib.request.urlopen(request)
print(response.read())