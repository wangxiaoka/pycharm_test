# -*- coding: utf-8 -*-
import struct
import binascii
values = ('FFFF', '0001', '1201')
class item:
	def __init__(self):
		self.Head = 'AAAA'
		self.Slot = 'FFFF'
		self.Type = '0001'
		self.Cmd  = ''
		self.Sata = 'FFFF'
		self.num  = ''
		self.para1 = ''
		self.para2 = ''
		self.Crc  = ''

cmd_get = item()
cmd_get.Cmd = '1201'
cmd_get.num = '0001'
cmd_get.para1= '0000'
cmd_get.para2= '000F'

s = struct.Struct('4s')
packed_data = s.pack(cmd_get)
print binascii.hexlify(packed_data)

print cmd_get

