import numpy as np

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def idf(term, docs):
    count = 0
    for doc in docs:
        if term in doc:
            count += 1
    return np.log10(len(docs) / count) + 1

for term in terms:
    print("idf({0}) = {1}".format(term, idf(term, docs)))