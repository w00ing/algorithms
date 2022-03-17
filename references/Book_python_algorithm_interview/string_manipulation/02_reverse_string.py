# 138
# https://leetcode.com/problems/reverse-string/

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

"""
INPUT: ["h","e","l","l","o"]
OUTPUT: ["o","l","l","e","h"]
"""

"""
INPUT: ["H","a","n","n","a","h"]
OUTPUT: ["h","a","n","n","a","H"]
"""


from typing import List

# Solution 1: Two Pointer swapping
def reverse_string_two_pointers(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right += 1


# Solution 2: Pythonic way
def reverse_string_pythonic_way(s: List[str]) -> None:
    s.reverse()
    # or s[:] = s[::-1]
