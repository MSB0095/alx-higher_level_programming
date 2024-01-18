#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    o = sys.argv[2]
    b = int(sys.argv[3])
    if o == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif o == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif o == "\*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif o == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
