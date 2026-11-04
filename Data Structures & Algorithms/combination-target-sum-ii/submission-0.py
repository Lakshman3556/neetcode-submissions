class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        def findCombinations(ind, target, ds):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findCombinations(i + 1, target - candidates[i], ds)
                ds.pop()
        findCombinations(0, target, [])
        return ans
        