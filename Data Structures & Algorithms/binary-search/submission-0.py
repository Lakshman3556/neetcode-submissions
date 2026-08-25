class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        m=(l+h)//2
        while l<=h:
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1
            m=(l+h)//2
        return -1                

        