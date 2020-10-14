import sys
import time


def instructions(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 12)


instructions('''\033[91m[!]\033[00mScript Spam Call
Run: python3 indo_call.py''')
