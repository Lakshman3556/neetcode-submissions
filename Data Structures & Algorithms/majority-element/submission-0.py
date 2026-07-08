class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]]+=1
        for k,v in dic.items():
            if v>(len(nums)/2):
                return k 