# 138
# https://leetcode.com/problems/longest-palindromic-substring/

"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


import collections
from typing import List

# Solution: expand palindrome from the center
def longest_palindromic_substring(s: str) -> str:
    # Determine if it is palindrome, and expand
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    # Return if it is palindrome to begin with
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""
    # Move the sliding window to the right
    for i in range(0, len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result
