
import os


people = {
	'Alice': {
		'phone': '1234',
		'addr': 'Foo drive 23'
	},
	'Beth' :{
		'phone':'2234',
		'addr' :'Bar street 43'
	},
	'Cecil' : {
	'phone' : '3234',
	'addr'  : 'Baz avenue 90'
	}
}

labels = {
	'phone' : 'phone number',
	'addr'  : 'address'
}

name = raw_input('Name: ')
request = raw_input('phone number(p) or address(a)?')

if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

#print name
#print labels[key]
#print people[name][key]

if name in people : print "%s's %s is %s." %(name, labels[key], people[name][key])