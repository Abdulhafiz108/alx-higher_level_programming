#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    sum = 0
    if i == 1:
        print("0")
    else:
        for j in range(1, i):
            sum += int(sys.argv[j])
        print("{}".format(sum))
