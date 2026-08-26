class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        h=x
        while l<=h:
            m=(l+h)//2
            if m**2==x:
                return m
            elif m**2>x:
                h=m-1
            else:
                l+=1
        return l-1               
