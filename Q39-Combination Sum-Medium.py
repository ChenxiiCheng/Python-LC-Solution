'''
Question: 
  39. Combination Sum

Descrition: 
  Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
  find all unique combinations in candidates where the candidate numbers sums to target.

  The same repeated number may be chosen from candidates unlimited number of times.

  Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Examples:
  1.Input: candidates = [2,3,6,7], target = 7,
	A solution set is:
	[
	  [7],
	  [2,2,3]
	]

  2.Input: candidates = [2,3,5], target = 8,
	A solution set is:
	[
	  [2,2,2,2],
	  [2,3,3],
	  [3,5]
	]	
'''

#Python3 Code:

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #Solution 2
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)
        
        
        #Solution
        candidates.sort()
        stack = [(0, 0, [])]
        ans = []
        while stack:
            total, index, res = stack.pop()
            if total == target:
                ans.append(res)
            for i in range(index, len(candidates)):
                t = total + candidates[i]
                if t > target:
                    break
                stack.append((t, i, res + [candidates[i]]))
        return ans

        