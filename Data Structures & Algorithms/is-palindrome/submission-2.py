class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=re.sub(r"[^a-zA-Z0-9]","",s).lower()
        l=0
        r=len(res)-1
        while l<=r:
            if res[l]!=res[r]:
                return False
            l+=1
            r-=1
        return True        



