class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=1
        nums.sort()
        lst=[]
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                c+=1
            else:
                if c>(len(nums)//3):
                    lst.append(nums[i])
                c=1
        if c>len(nums)//3:
            lst.append(nums[-1])        
        return lst            

        