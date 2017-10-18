# -*- coding: utf-8 -*-
import os

path = "C:\\Program Files (x86)\\Keysight\\BenchVue\\Platform\\BenchVue\\Keysight BenchVue.exe"
path = path.decode('utf8')

path1 = "D:\\Program Files (x86)\\KuGou\\KGMusic\\"
filename = "KuGou.exe"
path1 = path1.decode('utf8')
os.chdir(path1)
kugou = os.system(filename)
print "ok"
print kugou


