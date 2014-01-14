from sys import argv

script, file_name = argv

line1 = "This is line 1"
line2 = "This is line 2"
line3 = "This is line 3"

target = open(file_name, 'w')

target.write('%r \n%r\n%r\n' % (line1, line2, line3))

target.close()
