# From wiki.pythonchallenge.com
# Using Regular Expressions module

import re
strFile = open("equality.txt",'r')
text = strFile.read()

# A simple re solution
print "".join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text))
'''[A-Z]{3} means exactly 3 capital letters. The brackets () are used to define groups. 
For each matching pattern, only the group is returned. '''

# A better re method
print "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))
'''because when it says EXACTLY, there could be special characters 
that still solve the problem (eg. "?ABCdEFG#"). '''

# An even better re solution
print "".join(x[1] for x in re.findall('(^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}([^A-Z]|$)', text))

# The same, only using (?:) to exclude parenthesis from showing up in the rsult list
print "".join(re.findall('(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?:[^A-Z]|$)', text))

# Self-contained solution with RE
import urllib
print ''.join(re.findall(  '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',
  urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()))
