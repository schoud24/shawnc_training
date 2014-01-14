from sys import argv

#pass filename through argv argument
script, filename = argv

#anytime txt is referenced, it will open the variable
#'filename'

txt = open(filename)

#names the file you entered in the argv,
#and then txt calls the read function of that filename
print "Here's your file %r" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
