class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        if len(strs)==0:
            return [[""]]    
        res=[]
        for i in range(len(strs)):
            s=[]
            for j in range(i,len(strs)):
                if sorted(strs[i])==sorted(strs[j]) and not any(strs[j] in s for s in res):
                    s.append(strs[j])
            if len(s)>=1:        
                res.append(s)  
        return res            
