#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argcount = len(argv) - 1
    if argcount == 0:
        print("0")
    elif argcount > 0:
        sum = 0
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print("{}".format(sum))
