class Solution:
    def combinationSum(self, nums: List[int], tgt: int) -> List[List[int]]:
        res=[]
        def cs(idx,arr,tgt):
            if idx==len(nums):
                if tgt==0:
                    res.append(arr[:])
                return
            if nums[idx]<=tgt:
                arr.append(nums[idx])
                cs(idx,arr,tgt-nums[idx])
                arr.remove(nums[idx])
            cs(idx+1,arr,tgt)
        arr=[]
        cs(0,arr,tgt)
        return res                
