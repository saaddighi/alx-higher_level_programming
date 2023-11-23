#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if not args:
        print("0")
    else:
        result = sum(int(arg) for arg in args)
        print(result)

