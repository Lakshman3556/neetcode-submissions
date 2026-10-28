class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def se(idx,arr):
            if idx==len(nums):
                res.append(arr[:])
                return 
            arr.append(nums[idx])
            se(idx+1,arr)
            arr.remove(nums[idx])
            se(idx+1,arr)
        arr=[]
        se(0,arr)
        return res    