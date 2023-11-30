#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    sums = 0
    L = len(sys.argv) - 1
    for i in range(1, L + 1):
        sums += int(sys.argv[i])
    print(sums)
