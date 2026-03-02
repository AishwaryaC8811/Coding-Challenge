import sys
import math
import string


T_line = sys.stdin.readline().rstrip()
sentence = sys.stdin.readline().rstrip()

T = int(T_line)
for i in range(T):

    vowelCount = 0

    for letter in sentence:
        if letter == "a" or letter =="e" or letter == "i" or letter == "o" or letter == "u":
            vowelCount = vowelCount + 1

    print("Vowel Count: ", vowelCount)