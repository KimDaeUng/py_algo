# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # 포인터
        # start, end
        # if end 포인터에 해당하는 문자열이 범위 내에 있는 경우
        # => start 포인터 += 1 (단 end 포인터에 도달하기 전까지만) & answer 갱신
        # else
        # => end 포인터 += 1
                                    
        start_idx = end_idx = 0
        
        # 각 단어가 언제 등장했었는지를 알아야함
        memory = defaultdict(int)
        memory[s[0]] = 0
        
        for idx in range(len(s)):
            cur_char = s[idx]
            if cur_char not in memory:
                if end_idx < len(s):
                    end_idx += 1
                memory[cur_char] = end_idx
            else:
                if start_idx != 0 and start_idx < end_idx:
                    start_idx += 1
                    end_idx += 1
                memory[cur_char] = start_idx
        
        return end_idx - start_idx + 1

    def lengthOfLongestSubstring(self, s: str) -> int:

        used = {}
        max_length = 0

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
                
            used[char] = index
        
        return max_length