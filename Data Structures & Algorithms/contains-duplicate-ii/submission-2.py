class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        for r in range(1,len(nums)):
            while k<(r-l):
                l+=1
            for i in range(l,r):
                if nums[i]==nums[r] and abs(l-r)<=k:
                    return True          
        return False
                                
        