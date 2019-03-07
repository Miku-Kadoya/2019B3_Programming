import numpy as np

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

a = np.zeros((len(docs), len(terms)))

def tf(term, doc):
    count = 0
    for word in doc:
        if (word == term):
            count += 1
    return count / len(doc)

def idf(term, docs):
    count = 0
    for doc in docs:
        if term in doc:
            count += 1
    return np.log10(len(docs) / count) + 1

for i, doc in enumerate(docs):
    for j, term in enumerate(terms):
        a[i][j] = tf(term, doc) * idf(term, docs)

print(a)