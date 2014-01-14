formatter = "%r, %r, %r"

tabby_cat = "I'm tabbed in."
persian_cat = "I'm split on a line."
backslash_cat = "I'm a cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print formatter % (tabby_cat, persian_cat, backslash_cat)
print fat_cat
