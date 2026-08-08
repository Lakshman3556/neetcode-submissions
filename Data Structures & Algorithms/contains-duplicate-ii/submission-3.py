class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        w=set()
        for r in range(len(nums)):
            while k<(r-l):
                w.remove(nums[l])
                l+=1
            if nums[r] in w:
                return True
            w.add(nums[r])         
                   
        return False
                                
        