class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ls=[]
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        # Sort dictionary items by frequency in descending order
        temp = sorted(d.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            ls.append(temp[i][0])
        return ls        