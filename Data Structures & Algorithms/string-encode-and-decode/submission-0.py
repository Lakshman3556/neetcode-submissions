class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in range(len(strs)):
            n=len(strs[i])
            s+=str(n)
            s+='#'
            s+=strs[i]
        return s    
    def decode(self, s: str) -> List[str]:
        lst=[]
        n=0
        while n<len(s):
            num=""
            while s[n]!='#':
                num+=s[n]
                n+=1
            a=int(num)
            n+=1
            num=s[n:a+n]
            lst.append(num)
            n+=a
        return lst    
