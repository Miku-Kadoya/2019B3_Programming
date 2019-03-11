<<<<<<< HEAD
str = input()

=======
def ngram(str,n):
    ngram = []
    for i in range(len(str) - n + 1):
        ngram.append(str[i:i+n])
    return ngram

str = input()
word = str.split(' ')
char = "".join(word)
print('単語bi-gram: ' , ngram(word,2))
print('文字bi-gram: ' , ngram(char,2))
>>>>>>> origin/master
