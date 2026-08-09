class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxi=0
        for r in range(len(prices)):
            if prices[r]<prices[l]:
                l=r
            else:
                maxi=max(prices[r]-prices[l],maxi)
        return maxi                    

        
        