class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sub=[]
        def su(idx,arr):
            if idx==len(nums):
                sub.append(arr[:])
                return 
            arr.append(nums[idx])
            su(idx+1,arr)
            arr.remove(nums[idx])
            su(idx+1,arr)
        arr=[]
        su(0,arr)
        total = 0
        for subset in sub:
            xor_val = 0
            for num in subset:
                xor_val ^= num
            total += xor_val

        return total    