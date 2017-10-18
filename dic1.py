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

key = request
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

#print name
#print labels[key]
#print people[name][key]
person = people.get(name,{})
print person
print name



label = labels.get(key,key)
result = person.get(key,'not available')

#if name in people : print "%s's %s is %s." %(name, label, result)

print "%s's %s is %s." %(name, label, result)

print people