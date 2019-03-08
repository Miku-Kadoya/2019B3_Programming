str ='パタトクカシーー'
str1 = ''
str2 =''
for i in range(len(str)):
    if (i % 2 == 0):
        str1 += str[i]
    else:
        str2 += str[i]

print(str1)
print(str2)
