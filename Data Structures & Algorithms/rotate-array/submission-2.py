class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        for _ in range(k):
            l=n-1
            r=n-2
            while r>=0:
                nums[l],nums[r]=nums[r],nums[l]
                l-=1
                r-=1