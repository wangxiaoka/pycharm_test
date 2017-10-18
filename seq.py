database = [
    ['goushi','1234'],
    ['goushi1', '2234'],
    ['goushi2', '3234'],
    ['goushi3', '4234'],
]

username = raw_input("input a username:")
pin      = raw_input("input a pin:")

if [username,pin] in database:
    print "logined"
else:
    print "passward error!"