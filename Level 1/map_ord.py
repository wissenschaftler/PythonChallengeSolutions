# The URL of this level is http://www.pythonchallenge.com/pc/def/map.html
# using ord()
initStr = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''
fnlStr = []
for i in initStr:
    if 97 <= ord(i) <= 122:
        i = chr((ord(i)+1)%122+1+(ord(i)+1)/122*96)
    fnlStr.append(i)
print ''.join(fnlStr)
