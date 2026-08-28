class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(m,piles):
            s=0
            for i in piles:
                s+=math.ceil((i/m))
            return s
        l=1
        r=max(piles)
        while l<=r:
            m=(l+r)//2
            if time(m,piles)<=h:
                r=m-1
            else:
                l=m+1
        return l                    