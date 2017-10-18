_metaclass_ = type

class Person:

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def greet(self):
		print "Hello,world! I'm %s" % self.name

foo = Person()
foo.setName('Luke')
foo.greet()

print foo.name