class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def pp(idx,a):
            if idx==len(s):
                res.append(a[:])
                return
            for i in range(idx,len(s)):
                sub=s[idx:i+1]
                if sub==sub[::-1]:
                    a.append(sub)
                    pp(i+1,a)
                    a.pop() 
        pp(0,[])
        return res               