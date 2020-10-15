

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 분할 탐색?
        # 이진 탐색 - O(log n)
        
        # 리스트입력받아 좌우분할된 부분 각각에 찾는 문자열이 있는지 확인
        ret = []
        
        def recur(nums, target, s, e, m, ret):
            start  = s
            end = e
            middle = int(((end-start)+1) // 2)
            print(middle)
            
            # 상단
            if target > nums[middle]:
                start = middle + 1
                middle = ((end-start)+1) // 2
            
            # 하단 
            elif target < nums[middle]:
                end = middle - 1
                middle = ((end-start)+1) // 2
                
            # 일치
            elif target == nums[middle]:
                start = middle + 1
                ret.append(middle)
                middle = ((end-start)+1) // 2

            ret += recur(nums, target, start, end, middle, ret)
            
            return ret
        
        start  = 0
        end = len(nums)
        middle = ((end-start)+1) // 2

        ret = recur(nums, target, s=0, e=end, m=middle, ret=ret)
        
        answer     = [-1, -1]
        answer[0]  = ret[0]
        answer[-1] = ret[-1]
        
        return answer

                
#                 for i in range(start, end+1, 1):
#                     if nums[i] == target:
#                         ret.append(i)
#                         middle = ((end-i)+1) // 2
#                         recur(nums[i+1:], target, i, end, middle)

                


class Solution:
    def searchRange(self, nums, target):
        # 좌우로 분할탐색
        # 찾는 숫자가 나올떄까지 재귀,
        # 

        def recur(start, end, target):
            while start < end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid
            return start
        
        L = recur(0, len(nums))
        
        
        
# Solution

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary Search
        
        ret = [-1, -1]
        if len(nums) == 0:
            return ret
        
        
        left = 0
        right = len(nums) - 1 
        
        # 1. middle index 가 target 과 크거나 같도록 탐색 : 상한에 middle 포함
        while  left < right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1 # middle != target 이므로 + 1 한 값을 할당
            
            
        # target 값과 일치하는 인덱스를 찾았을 경우
        if nums[right] != target:
            return ret
            
        ret[0] = right
        
        # 2. middle index 가 target 과 작거나 같도록 탐색 : 하한에 middle 포함

        right = len(nums) - 1
        
        while left < right:
            # 1을 더해야 앞에서 탐색한 인덱스와 겹치지 않음??
            middle = (left + right + 1) // 2
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle
                
        if nums[left] != target:
            return ret
        
        ret[1] = left
        
        return ret