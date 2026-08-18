class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        stk=[]
        for i in range(len(temp)):
            while stk and temp[stk[-1]]<temp[i]:
                t=stk.pop()
                res[t]=i-t
            stk.append(i)
        return res        



        