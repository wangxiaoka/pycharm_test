def story(**kwds):
	return 'Once upon a time, there is a '\
			'%(job)s called %(name)s.' %kwds

def power(x, y, *Others):
	if Others:
		print 'Received redundant parameters: ',Others
	return pow(x, y)

def interval(start, stop = None, step = 1):
	'Imitates range() for step > 0 '
	if stop is None:
		start, stop = 0, start
	result = []
	i = start
	while i < stop:
		result.append(i)
		i += step
	return result

print story(job = 'King', name = 'Gumby')

print story(name = 'Sir Robin', job = 'brave knight')

param = {'job':'language','name':'Python'}

print story(**param)

del param['job']
print param
print story(job='stroke of genius',**param)
print power(2,3)
print power(3,2)
print power(x=3,y=2)
param = (5,) * 2
print power(*param)
print interval(3,7)
print power(*interval(3,7))