# -*- coding: utf-8 -*-
import binascii
def FrameCmd(type, cmd, ParaNum, Para):
	Head = 'AAAA'
	slot = 'FFFF'
	Stat = 'FFFF'

	list = Head + slot + type + cmd + Stat + ParaNum + Para
	print list[4:12]
	print list[12:20]

	str1 = bytearray.fromhex(list[4:12])
	print str1
	print binascii.b2a_hex(str1)

	str2 = bytearray.fromhex(list[12:20])
	print str2
	print binascii.b2a_hex(str2)

	str3 = str2

	for i in range(len(str1)):
		str3[i] = str1[i] ^ str2[i]
	print str3
	print binascii.b2a_hex(str3)
	str33 = binascii.b2a_hex(str3)

	Frame = list + str33.upper()
	return Frame


if __name__ == '__main__':
	print FrameCmd('0001', '1201', '0001', '0000000F')
	frame = bytearray.fromhex(FrameCmd('0001', '1201', '0001', '0000000F'))
	print frame



