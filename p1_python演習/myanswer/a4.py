str ='パタトクカシーー'
str1 = ''
str2 =''
for i in range(len(str)):
    if (i % 2 == 0):
        str1 += str[i:(i+1)]
    else:
        str2 += str[i:(i+1)]

print(str1)
print(str2)