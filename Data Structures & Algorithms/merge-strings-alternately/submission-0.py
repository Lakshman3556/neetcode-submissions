class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=0
        l2=0
        r=""
        while l1<=len(word1)-1 and l2<=len(word2)-1:
            r+=word1[l1]
            r+=word2[l2]
            l1+=1
            l2+=1
        if l1<=len(word1):
            r+=word1[l1:len(word1)]
        if l2<=len(word2):
            r+=word2[l2:len(word2)]
        return r          

