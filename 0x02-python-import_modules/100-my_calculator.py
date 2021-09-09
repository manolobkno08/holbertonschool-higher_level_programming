#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':

    args = len(argv) - 1

    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    func = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in func:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, op, b, func[op](a, b)))
