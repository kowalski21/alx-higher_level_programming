#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    "Print infinite addition"
    import sys

    sum_total = 0
    for idx in range(len(sys.argv) - 1):
        sum_total += int(sys.argv[idx + 1])
    print("{}".format(sum_total))
