import numpy as np
from nlp.a15 import tf_idf
from nlp.a16 import cosine_sim

with open("dataset/data.txt", "r") as f:
    docs = []
    terms = []
    for line in f:
        line = line.rstrip('\n')
        docs.append(line.split("と"))

    for i in docs:
        terms += i
terms = list(set(terms))

tfidf = tf_idf(docs, terms)
a = np.zeros((len(docs), len(terms)))
for i in range(len(docs)):
    for j in range(len(docs)):
        a[i][j] = cosine_sim(tfidf[i], tfidf[j])
print(a)