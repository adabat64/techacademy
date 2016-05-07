import pickle

def save(doc):
    pickle.dump(doc, open("list.p", "wb"))


def load():
    return pickle.load(open("list.p", "rb"))
