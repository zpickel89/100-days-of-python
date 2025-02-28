""" 
Heads or tails
    Does a coin flip
"""

import random

# note random() does NOT include 1
result = random.randint(0, 1)

if result == 1:
    print("Heads")
else:
    print("Tails")