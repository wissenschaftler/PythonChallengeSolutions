# The URL of this level: http://www.pythonchallenge.com/pc/def/equality.html
# Character by character processing，without using re module
# Written by Wei Xu
strFile = open("equality.txt",'r') # equality.txt is where the data is
wholeStr = strFile.read()
countLeft = 0  # the number of consecutive capital letters on the left side of a small letter
countRight = 0  # the number of consecutive capital letters on the right side of a small letter
left3 = False  # whether there are 3 consecutive capital letters on the left side of the considered small letter
leftCap = False  # whether the previous letter is capital
resultTemp = []  # preparatory list for the final result
result = []  # the final result
for i in wholeStr:
    # if i is capital and its left letter is small
    if (not leftCap) and (65 <= ord(i) <= 90):
        leftCap = True  
	# If i's left small letter is preceded by three consecutive capital letters，then that small letter is our candidate
        # and we start to count the number of consecutive capital letters on its right
	# Otherwise we treat i as the capital letter on the left side of the next small letter
        if left3:
            countRight += 1
        else:
            countLeft += 1
    # if i is capital and its left letter is capital
    elif leftCap and (65 <= ord(i) <=90):
        if left3 and (countRight < 3):
            countRight += 1
        # if countRight>3，then stop counting countRight since it would be useless，but instead assign its value to countLeft
        elif countRight == 3:
            countLeft = countRight
            countRight += 1  # simply to bypass the check of countRight == 3 in Line 37
            countLeft += 1
            resultTemp.append('0') # the 0's and its left letter will be ignored when getting the final result
        else:
            countLeft += 1
    # if i is small
    elif (122 >= ord(i) >= 97):
        leftCap = False  
        if (countLeft == 3) or (countRight == 3):
            left3 = True
            resultTemp.append(i)  
        elif left3:
            left3 = False
            resultTemp.append('0') 
        countLeft = 0
        countRight = 0
# get result from resultTemp，i.e. ignoring 0's and its preceding single small letter
prev='0'
for j in resultTemp:
    if (j !=  '0') and (prev != '0'):
        result.append(prev)
    prev = j
if (prev != '0') and (countRight == 3):
    result.append(j)
print ''.join(result)
