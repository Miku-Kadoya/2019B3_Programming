str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str = str.replace('.', '').replace(',', '')
words = str.split()
l = list()
for i in range(len(words)):
    l.append(len(words[i]))
print(l)
