# https://leetcode.com/problems/merge-intervals/description/

# My solution : Fail
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        intervals 내 연속된 2개의 sample씩 끝과 시작을 비교
        예를 들어
        itv[i] = [1, 3]
        itv[i+1] = [2, 6]
        라할 때
        itv[i][1] >= itv[i+1][0] 이면
        itv_new = [itv[i][0], itv[i+1][1]]
        로 intervals의 해당 위치에 저장
        itv[i], itv[i+1]은 삭제

        # 예외?
        1. 원소가 없거나 하나인 경우 -> 그대로 리턴
        2. 원소가 2개인데 merge 안될 때 -> 그대로 리턴
        3. 뒤의 interval이 앞쪽 interval을 포함할 경우[[1, 4], [0, 4]]
        '''
        def search(itv1, itv2, intervals):
            new_itv = [None, None]

            # 새 interval의 하한
            # 두 구간이 가운데서 겹치고
            if (itv2[0] <= itv1[1]):
                # 새 interval의 하한
                # 뒤 itv의 하한이
                #   앞 itv의 하한 보다 작으면
                if itv2[0] < itv1[0]:
                    new_itv[0] = itv2[0]
                #   앞 itv의 상한이 더 작으면
                else:
                    new_itv[0] = itv1[0]
                
                # 새 interval의 상한
                # 앞 itv의 상한이
                #   뒤 itv의 상한 보다 크면
                if itv2[1] <= itv1[1]:
                    new_itv[1] = itv1[1]
                #   뒤 itv의 상한이 더 크면
                else:
                    new_itv[1] = itv2[1]

                return [new_itv]
            
            # 구간이 겹치지 않는다면
            else:
                # 앞에것만 그대로 붙임.
                # 뒤에것은 뒤에서 판단
                # 만약 이게 intervals의 마지막 index라면

                if itv2 == intervals[-1]:
                    return [itv1, itv2]
                else:
                    # 앞에서 merge가 이뤄졌다면 패스
                    if answer[-1][1] == itv1[1]:
                        return []
                    else:
                        return [itv1]

        len_intervals = len(intervals)
        if len_intervals <= 1:
            return intervals
        answer = []
        for i in range(len_intervals-1):
            print(i)
            print('itv[i]   :', intervals[i])
            print('itv[i+1] :', intervals[i+1])

            if (intervals[i] == [0,0]) or (intervals[i+1] == [0,0]):
                return intervals

            answer += search(intervals[i], intervals[i+1], intervals)
        
        return answer

        

       len_intervals = len(intervals)
        if len_intervals <= 1:
            return intervals

        answer = []
        overlap_before = False
        for i in range(len_intervals-1):
            
            # Check overlaps
                
                
            print(i)
            print('itv[i]   :', intervals[i])
            print('itv[i+1] :', intervals[i+1])
            if intervals[i][1] >= intervals[i+1][0]:
                if overlap_before:
                    new_itv = [answer[-1][0], intervals[i+1][1]]
                else:
                    new_itv = [intervals[i][0], intervals[i+1][1]]
                print("Overlaps are founded")
                answer.append(new_itv)
                overlap_before = True
                print("answer :", answer)

            else:
                if len_intervals == 2:
                    return intervals

                if overlap_before:
                    answer.append(intervals[i+1])
                else:
                    # 직전에 overlap이 일어나지 않았다면
                    # 다음원소가 그냥 추가되었을 것이므로 
                    if intervals[i] == answer[-1]:
                        answer.append(intervals[i+1])
                    else:
                        print("???")
                        answer.append(intervals[i])
                overlap_before = False
                print("No Overlaps")
                print("answer :", answer)

                continue
        return answer

# Solution
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