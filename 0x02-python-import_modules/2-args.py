#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments:".format(argc))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
