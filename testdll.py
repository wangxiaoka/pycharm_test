# -*- coding: utf-8 -*-
import ctypes

path = r'C:\Windows\System32\testdll.dll'
# d = ctypes.CDLL(path)
d = ctypes.WinDLL(path)
# dll = ctypes.cdll.LoadLibrary(path)
ret = d.IntAdd(2, 4)
print ret

# a = Objdll.scanf()
# print a
