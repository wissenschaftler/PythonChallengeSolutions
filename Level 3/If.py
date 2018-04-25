# From wiki.pythonchallenge.com
# Straightforward and visually impressive, but didn't catch the edge cases

import string
strFile = open("equality.txt",'r')
data = strFile.read()
i,a,b,c=0,'','',''
for a in data:
	if data[i] in string.lowercase[:26]:
		if data[i+1] in string.uppercase[:26]:
			if data[i+2] in string.uppercase[:26]:
				if data[i+3] in string.uppercase[:26]:
					if data[i+4] in string.lowercase[:26]:
						b=b+data[i+4]
						if data[i+5] in string.uppercase[:26]:
							if data[i+6] in string.uppercase[:26]:
								if data[i+7] in string.uppercase[:26]:
									if data[i+8] in string.lowercase[:26]:
										c=c+b[-1]
	i=i+1
print c
