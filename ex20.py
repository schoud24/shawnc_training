from sys import argv

script, input_file = argv

#print all function is defined to print whatever is 'f'
def print_all(f):
	print f.read()

#rewind is defined to seek 
def rewind(f):
	f.seek(0)

#print a line that says what the line_count is and then will display what's on that line
def print_a_line(line_count, f):
	print line_count, f.readline()

#current_file reads the data found in the input_file
current_file = open(input_file)

#prints the file prior to rewind
print "First let's print the whole file:\n"

print_all(current_file)

#executes rewind, which takes the file data and seeks to the first byte of the file
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)