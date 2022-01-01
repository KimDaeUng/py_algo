# https://leetcode.com/problems/valid-palindrome
# 3m
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('[^\da-z]', '', s.lower())
        reverse_s = s[::-1]
        if s == reverse_s:
            return True
        else:
            return False