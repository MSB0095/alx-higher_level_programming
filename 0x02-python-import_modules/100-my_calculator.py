#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = sys.argv[2]
    c = int(sys.argv[1])
    if b == "+":
        print("{} + {} = {}".format(a, c, add(a, c)))
    elif b == "-":
        print("{} - {} = {}".format(a, c, sub(a, c)))
    elif b == "*":
        print("{} * {} = {}".format(a, c, mul(a, c)))
    elif b == "/":
        print("{} / {} = {}".format(a, c, div(a, c)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
