# -*- coding: utf-8 -*-
from urllib import urlopen
from urllib import urlretrieve
import re
webpage = urlopen("http://www.python.org")

urlretrieve('http://www.baidu.com', 'd:\\baidu.html')
text = webpage.read()
m = re.search('<a href="([^"]+)" .*?>about</a>', text,re.IGNORECASE)
print m.group(1)
print webpage