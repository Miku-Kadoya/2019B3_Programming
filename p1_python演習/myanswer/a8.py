str = 'Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
str = str.replace('.', '')
words = str.split()
for i in range(len(words)):
    if (i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18):
        words[i] = words[i][:1]
    else:
        words[i] = words[i][:2]

dict = {s: (words.index(s) + 1) for s in words}
print(dict)