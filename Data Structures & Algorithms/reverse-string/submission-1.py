class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=0
        r=len(s)-1
        def reverse(l,r):
            if l>r:
                return
            s[l],s[r]=s[r],s[l]
            reverse(l+1,r-1)
        return reverse(l,r)            

        