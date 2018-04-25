# The URL of this level: http://www.pythonchallenge.com/pc/def/ocr.html
strFile = open("ocr.txt",'r') #ocr.txt is where the data is
wholeStr = strFile.read() 
fnlStr = []
for i in wholeStr:
    if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
         fnlStr.append(i)
print ''.join(fnlStr)
