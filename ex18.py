def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin'."

def print_three(arg1, arg2, arg3):
	print "%r, %s, %r" % (arg1, arg2, arg3)
	
print_two("Shawn", "Choudhury")
print_two_again("Sean", "Jean")
print_one("First!")
print_none()
print_three("Sup", "My", "Brotha?")
