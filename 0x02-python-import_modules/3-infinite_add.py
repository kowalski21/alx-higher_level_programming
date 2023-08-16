#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    "Print infinite addition of arguments on command line"
    import sys

    sum_total = 0
    for num in range(len(sys.argv) - 1):
        next_num = int(sys.argv[num + 1])
        sum_total += next_num
    print("{}".format(sum_total))
