#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(ord('z'), ord('a') - 1, -1):
        print("{:c}".format(i - 32 if i % 2 == 0 else i), end="")

