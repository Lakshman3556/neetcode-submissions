class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        sc1={}
        sc2={}
        l=0
        for i in s1:
            sc1[i]=sc1.get(i,0)+1
        for i in range (len(s2)):
            sc2[s2[i]]=sc2.get(s2[i],0)+1
            while (i-l+1)>n:
                sc2[s2[l]]-=1
                if sc2[s2[l]]==0:
                    del sc2[s2[l]]
                l+=1    

            if sc1==sc2:
                return True
        return False            
                       
        