import sys

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def tf(term, doc):
    count = 0
    for word in doc:
        if (word == term):
            count += 1
    return count / len(doc)

for i in docs:
    for j in terms:
        sys.stdout.write ("tf({0}, {1}) = {2} ".format(j, i, tf(j, i)))
    print()