# -*- coding: utf-8 -*-
import ctypes

path = 'C:\Windows\System32\msvcrt.dll'

Objdll = ctypes.windll.LoadLibrary(path)

Objdll.printf(b'hello world!\n')

# a = Objdll.scanf()
# print a
