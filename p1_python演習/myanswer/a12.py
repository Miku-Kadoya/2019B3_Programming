with open("dataset/data.txt", "r") as f:
    docs = []
    terms = []
    for line in f:
        line = line.rstrip('\n')
        docs.append(line.split("と"))

    for i in docs:
        terms += i
    terms = list(set(terms))
    print("docs : ", docs)
    print("terms : ", terms)

f.close()