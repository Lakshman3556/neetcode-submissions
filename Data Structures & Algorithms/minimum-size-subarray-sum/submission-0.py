class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        mini=float('inf')
        l=0
        if sum(nums)<k:
            return 0
        c=0    
        for i in range(len(nums)):
            c+=nums[i]
            while c>=k:
                mini=min(mini,i-l+1)
                c-=nums[l]
                l+=1
        return mini        

        