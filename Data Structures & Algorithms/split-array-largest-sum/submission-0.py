class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split(nums,mid):
            l=1
            su=0
            for i in range(len(nums)):
                if su+nums[i]<=mid:
                    su+=nums[i]
                else:
                    l+=1
                    su=nums[i]
            return l
        l=max(nums)
        h=sum(nums)
        while l<=h:
            mid=(l+h)//2
            ndays=split(nums,mid)
            if ndays<=k:
                h=mid-1
            else:
                l=mid+1
        return l                

        