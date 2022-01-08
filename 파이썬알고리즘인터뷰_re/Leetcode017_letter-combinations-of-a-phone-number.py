# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from string import ascii_lowercase
class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        alphabets = tuple(ascii_lowercase)
        keypad = {
            "2" : alphabets[:3],
            "3" : alphabets[3:6],
            "4" : alphabets[6:9],
            "5" : alphabets[9:12],
            "6" : alphabets[12:15],
            "7" : alphabets[15:19],
            "8" : alphabets[19:22],
            "9" : alphabets[22:],
        }
        digits = list(digits)
        N = len(digits)
        
        # Base case
        if N == 0:
            return []
        
        self.results = []
        
        def build(string, depth):
            if depth == N:
                self.results.append(string)
                return 
            digit = digits[depth]
            for cand in keypad[digit]:
                build(string + cand, depth + 1)

        build(string='', depth=0)
        
        return self.results