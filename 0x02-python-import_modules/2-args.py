#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i < 2:
        print("0 arguments.")
    elif i == 2:
        print("1 argument:")
        print("{}: {}".format(i - 1, sys.argv[i-1]))
    else:
        print("{} arguments:".format(i - 1))
        for j in range(1, i):
            print("{}: {}".format(j, sys.argv[j]))
