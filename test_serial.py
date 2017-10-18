import serial
import serial.tools.list_ports

# ser = serial.Serial('com3',115200)
# print ser.portstr
# reslut1 = ser.isOpen()
# print reslut1
# strInput = raw_input('enter some words:')
# n = ser.write(strInput)
# print n
#
# str = ser.readline(n)
# print str
# ser.close()
# reslut = ser.isOpen()
# print reslut
plist = list(serial.tools.list_ports.comports())
print plist
print plist[0]
if len(plist) < 0:
	print "open com failed"
else:
	plist_0 = list(plist[0])
	serialName = plist_0[0]
	serialFD = serial.Serial(serialName,9600,timeout=10)
	print "check which port was really used > ",serialFD.name


strInput = raw_input("enter words: ")
n = serialFD.write(strInput)
print n
str = serialFD.read(n)
print str










