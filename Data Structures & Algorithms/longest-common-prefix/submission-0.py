class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r=sorted(strs,key=len)
        res=r[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(res):
                res=res[:-1]
                if not res:
                    return ""
        return res            

        