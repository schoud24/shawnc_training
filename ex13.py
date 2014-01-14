from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

first_variable = raw_input("what is your first variable? ")
second_variable = raw_input("what is your second variable? ")

print "Your first variable is %s and your second variable is %s." % (
first_variable, second_variable)
	
	