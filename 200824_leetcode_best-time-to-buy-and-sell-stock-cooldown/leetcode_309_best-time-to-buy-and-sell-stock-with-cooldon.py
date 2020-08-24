'''
1. Reference
- Leetcode 309. Best Time to Buy and Sell Stock with Cooldown [ Algorithm + Code Explained], https://youtu.be/w6xk5Po-DX0
- Leetcode 309. Best Time to Buy and Sell Stock with Cooldown (Python), https://zhenyu0519.github.io/2020/02/29/lc309/

2. Topic : DP

3. Methodology
- There're 3 status. But they can be converted into 2 DP Lists
    * Case 1 : We have a stock on day i, the list 'hold', max of the below : 
        - I boghut it today
            unhold[i-2] - prices[i]
                unhold[i-2] : 이틀 전의 주식 매도로 얻은 순익(실제 매도가 이루어지지 않았더라도 cool down day로 인해 이틀전을 고려해야함)
                - prices[i] : 당일매수주가. 매수로 인해 전체 이익에서 차감
                
        - I am carry forwading
            hold[i-1]
                : 주식 보유 상태로 유지하는 이익, 어제의 이익을 그대로 복사

    * Case 2 : We have no stock on day i, the list 'unhold', max of the bellow:
        - I sold it today
            hold[i-1][1] + prices[i]
                : 직전날 주식 보유 이익 + 당일매도주가

        - I am carry forwarding, doing nothing
            unhold[i-1][0]
                : 주식 미보유상태로 유지하는 이익, 어제의 이익을 그대로 복사
- The answer should be when you not hold the stock. -> Case2(the list 'unhold')'s last value


'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        len_prices = len(prices)
        
        # [Exception hadnling] : the length of prices list <= 2
        if len_prices <= 1:
            return 0
        if len_prices == 2 & prices[1] > prices[0]:
            return prices[1]-prices[0]
        elif len_prices == 2 & prices[0] > prices[1]:
            return 0
        
        
        # When the length of prices list >= 3 
        hold = [0]*len_prices   
        unhold = [0]*len_prices 
        
        # initialize 0 th day profit
        unhold[0] = 0        
        hold[0] = -prices[0]
        
        # 1 th day profit
        # case 2 (Unhold List) : 둘째날 보유하지않음으로 생기는 이익
        # -> max(보유하지 않음으로 유지하는 직전날의 이익 (cool-down),
        #        오늘 매도 이익(sell) : 직전날보유이익+당일매도이익 )
        unhold[1] = max(unhold[0], hold[0]+prices[1])
        # case 1 (Hold List) : 둘째날 보유함으로 생기는 이익
        # -> max(보유함으로 유지하는 직전날 이익(cool-down),
        #        오늘 매수 이익(buy) : 이틀전매도로인해 얻은 이익-당일매수주가)
        hold[1] = max(hold[0], unhold[0]-prices[1])
        
        # 2 th day to last day profit
        for i in range(2, len_prices):
            unhold[i] = max(unhold[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], unhold[i-2] - prices[i])
        
        return unhold[-1]