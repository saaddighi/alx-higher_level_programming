#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    end = '' if i == ord('z') else ' '
    print("{}".format(chr(i)), end=end, flush=True)
