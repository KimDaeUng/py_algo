# https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        # 예외처리
        if len(intervals) < 2:
            return intervals
        
        # memory : 비교 기준
        # 데이터를 sort해두었으므로 하한 오름차 순으로 정렬됨
        # 따라서 각각의 interval과 비교기준 memory를 비교하여

        # 1) 겹치지 않으면 answer에 추가하고,
        #    비교기준을 현재 interval로 업데이트

        # 2) 겹칠경우 상한만 비교하여
        #    현재 interval이 더 클 경우 비교기준의 상한을 확장하고
        #    다음 interval로 넘어감

        memory = intervals[0]
        answer = []
        for interval in intervals:
            # 가운데가 겹치지 않을 때는
            if interval[0] > memory[1]:
                # 앞의 것을 result list에 붙이고
                answer.append(memory)
                # 비교 대상을 교체함
                memory = interval
            # 가운데가 겹칠 경우
            else :
                # 뒤의 것의 상한이 더 크면
                # 앞의 것의 상한을 업데이트
                memory[1] = max(memory[1],interval[1])
                
        # 최종적으로 추가되는 memory는
        # 겹치지 않았을 경우는 마지막 interval,
        # 겹친 경우는 merge된 interval
        answer.append(memory)
        return answer