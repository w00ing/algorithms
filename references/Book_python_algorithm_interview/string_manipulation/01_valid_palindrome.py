# 138
# https://leetcode.com/problems/valid-palindrome/

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

"""
INPUT: "A man, a plan, a canal: Panama"
OUTPUT: true
"""

"""
INPUT: "race a car"
OUTPUT: false
"""


import collections
import re
from typing import Deque

# Solution 1: Convert to list
# 304ms
def is_palindrome_using_list(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # check if palindrome
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


# Solution 2: Use deque
# 62ms
def is_palindrome_using_deque(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


# Solution 3: Use slicing
# 36ms
def is_paindrome_using_slicing(s: str) -> bool:
    s = s.lower()
    s = re.sub("[^a-z0-9]", "", s)

    return s == s[::-1]
