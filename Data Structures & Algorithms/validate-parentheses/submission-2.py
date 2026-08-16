class Solution:
    def isValid(self, s: str) -> bool:
        ls=[]
        if len(s)==1:
            return False
        for i in s:
            if i in '({[':
                ls.append(i)   
            elif i==')'and ls and ls[-1]=='(':
                ls.pop()
                continue
            elif i==']' and ls and ls[-1]=='[':
                ls.pop()
                continue
            elif i=='}' and ls and ls[-1]=="{":
                ls.pop()
                continue
            else:
                return False    
        if len(ls)!=0:
            return False
        else:            
            return True        

                    
        