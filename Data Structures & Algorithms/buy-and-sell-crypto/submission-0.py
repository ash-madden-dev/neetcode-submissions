class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = 100
        profit = 0
        for price in prices:
            if price <= lowest_price:
                lowest_price = price
            else:
                if profit < price - lowest_price:
                    profit = price - lowest_price
        return profit