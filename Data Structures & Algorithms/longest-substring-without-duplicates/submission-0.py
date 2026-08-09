class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w=set()
        l=0
        maxi=0
        for i in range(len(s)):
            while s[i] in w:
                w.remove(s[l])
                l+=1
            if s[i] not in w:
                w.add(s[i])
                maxi=max(maxi,i-l+1)    
        return maxi        
                


        