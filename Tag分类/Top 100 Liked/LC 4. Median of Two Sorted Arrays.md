### LC 4. Median of Two Sorted Arrays

[Link]: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

#### Question

![image-20190904181206662](/Users/chenxi/Library/Application Support/typora-user-images/image-20190904181206662.png)



#### Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Solution
        l = len(nums1) + len(nums2)
        if l % 2:  # the length is odd
            return self.findKthSmallest(nums1, nums2, l //2)
        else:
            return (self.findKthSmallest(nums1, nums2, l // 2 - 1) +
            self.findKthSmallest(nums1, nums2, l // 2)) * 0.5

    def findKthSmallest(self, A, B, k):
        # # force nums1 is not longer than nums2
        # if len(nums1) > len(nums2):
        #     return self.findKthSmallest(nums2, nums1, k)
        # if not nums1:
        #     return nums2[k - 1]
        # if k == 1:
        #     return min(nums1[0], nums2[0])
        # pa = min(k // 2, len(nums1)); 
        # pb = k - pa  # take care here
        # if nums1[pa - 1] <= nums2[pb - 1]:
        #     return self.findKthSmallest(nums1[pa:], nums2, k - pa)
        # else:
        #     return self.findKthSmallest(nums1, nums2[pb:], k - pb)
        
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            return self.findKthSmallest(A[:i], B[j:], i)
        else:
            return self.findKthSmallest(A[i:], B[:j], j)
```

