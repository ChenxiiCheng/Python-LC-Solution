**Question:**

1. Two Sum

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```



**Solution:**

法一：暴力解法

```javascript
var twoSum = function(nums, target) {
    //时间复杂度O(n)
    n = nums.length
    for (i = 0; i < n; i++) {
        for (j = 0; j < i; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];   
            }
        }
    }
    return [-1, -1];
}
```



法二：map存储每个(nums[i], i)

```javascript
var twoSum = function(nums, target) {
    let map = new Map;
    for (i = 0; i < nums.length; i++) {
        if (map.has(target - nums[i])) {
            return [map.get(target - nums[i]), i]
        } else {
            map.set(nums[i], i);
        }
    }
    return [-1, -1];
}
```

