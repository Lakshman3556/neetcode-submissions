class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0    
        c=1
        maxi=float('-inf')
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            elif nums[i+1]-nums[i]==1:
                c+=1
            else:
                maxi=max(c,maxi)
                c=1         
        return max(maxi,c)     
            