class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=re.sub(r"[^a-zA-Z0-9]","",s).lower()
        def isp(l,r):
            if l>=r:
                return True
            elif res[l]!=res[r]:
                return False
            return isp(l+1,r-1)
        return isp(0,len(res)-1)            


