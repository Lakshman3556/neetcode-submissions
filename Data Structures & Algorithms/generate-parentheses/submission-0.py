class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def ge(cu,op,cp):
            if len(cu)==2*n:
                res.append(cu)
                return
            if op<n:
                ge(cu+"(",op+1,cp)
            if cp<op:
                ge(cu+")",op,cp+1)
        ge("",0,0)
        return res            

                