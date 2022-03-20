# 138
# https://leetcode.com/problems/most-common-word/

"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.


Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"

Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
"""


import collections
from posixpath import split
import re
from typing import List

# Solution: Using List Comprehension, Counter object
def most_common_word(paragraph: str, banned: List[str]) -> str:
    words = [
        word
        for word in re.sub(r"[^\w", " ", paragraph).lower().split()
        if word not in banned
    ]

    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]
