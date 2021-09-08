#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    args = len(sys.argv)

    sum = 0

    if args == 0:
        print("0")
    else:
        for i in range(1, args):
            sum = sum + int(sys.argv[i])
        print("{}".format(sum))
