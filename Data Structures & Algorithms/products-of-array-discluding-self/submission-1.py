class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst=[]
        p=1
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            p*=nums[i]
        if 0 not in nums:        
            for i in range(len(nums)):
                s=int(p/nums[i])
                lst.append(s)
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1        
        if c == 1:
            for i in range(len(nums)):
                if nums[i]==0:
                    lst.append(p)
                else:
                    lst.append(0)
        if c>1:
            return [0]*len(nums)                       
        return lst        