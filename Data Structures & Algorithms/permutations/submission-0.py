class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def pc(arr,m):
            if len(arr)==len(nums):
                res.append(arr[:])
                return
            for i in range(len(nums)):
                if not m[i]:
                    m[i]=True
                    arr.append(nums[i])
                    pc(arr,m)
                    arr.remove(nums[i])
                    m[i]=False
        arr=[]
        m=[False]*len(nums)
        pc(arr,m)
        return res      
