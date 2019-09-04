### LC 1. Two Sum

[Link]: https://leetcode.com/problems/two-sum/description/

#### Question

![image-20190904173654883](/Users/chenxi/Library/Application Support/typora-user-images/image-20190904173654883.png)



#### Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Solution 2 - 字典
        dic = {}
        for idx, val in enumerate(nums):
            if (target - val) in dic:
                return [dic[target - val], idx]
            dic[val] = idx
        return [-1, -1]
        
        
        #Solution - 暴力解法
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
```



