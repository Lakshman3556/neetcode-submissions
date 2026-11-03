class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def ss(idx,arr):
            if idx==len(nums):
                if arr not in res:
                    res.append(arr[:])
                    return
                return
            arr.append(nums[idx])
            ss(idx+1,arr)
            arr.pop()
            ss(idx+1,arr)
        arr=[]
        ss(0,arr)
        return res            