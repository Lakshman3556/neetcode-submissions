class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def dayss(m,weights):
            s=0
            d=1
            for i in weights:
                if s+i<=m:
                    s+=i
                else:
                    d+=1
                    s=i
            return d
        h=sum(weights)
        l=max(weights)
        while l<=h:
            m=(l+h)//2
            if dayss(m,weights)<=days:
                h=m-1
            else:
                l=m+1
        return l                            