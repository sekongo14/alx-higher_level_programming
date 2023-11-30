#!/usr/bin/python3
if __name__ = "__main__":
    import hidden_4
    noms = dir(hidden_4)
    L = []
    for nom in noms:
        if nom[:2] != '__':
            L.append(nom)
    L1 = tuple(sorted(L))
    for name in L1:
        print(name)
