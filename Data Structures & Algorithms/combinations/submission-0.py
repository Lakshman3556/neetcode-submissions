class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def cb(arr,start):
            if len(arr)==k:
                res.append(arr[:])
                return
            for i in range(start,n+1):
                arr.append(i)
                cb(arr,i+1)
                arr.pop()
        arr=[]        
        cb(arr,1)
        return res