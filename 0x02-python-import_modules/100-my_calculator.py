#!/usr/bin/python3
# 100-my_calculator.py

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul

    arg_count = len(sys.argv) - 1

    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops_map = {"*": mul, "/": div, "+": add, "-": sub}
    if sys.argv[2] not in list(ops_map.keys()):
        print("Unknown operator. Available operators: +,-,* and /")
        sys.exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops_map[sys.argv[2]](a, b)))
