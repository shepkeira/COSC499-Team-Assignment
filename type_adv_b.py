import sys
import time
from random import random


# Pseudo-typing method, can use this instead of say(s) as desired
def type(s, t):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random() * t)
    print("")

# Default speed type


def default_type(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random() * 0.04)
    print("")
