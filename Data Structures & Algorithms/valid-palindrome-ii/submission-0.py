class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        def ispal(l,r):
            if l>=r:
                return True
            if s[l]!=s[r]:
                return False
            return ispal(l+1,r-1)
        while l<r:
            if s[l]!=s[r]:
                if ispal(l+1,r) or ispal(l,r-1):
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True                

