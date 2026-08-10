class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxif=0
        ans=0
        c={}
        for r in range(len(s)):
            c[s[r]]=c.get(s[r],0)+1
            maxif=max(maxif,c[s[r]])
            while (r-l+1)-maxif>k:
                c[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans        
                
