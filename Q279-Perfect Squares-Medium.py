'''
Question: 
  279. Perfect Squares

Descrition: 
   Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example:

  1.Input: n = 12
    Output: 3 
    Explanation: 12 = 4 + 4 + 4.

  2.Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.
'''

#Python code

class Solution:
    def numSquares(self, n: int) -> int:
        # BFS
        # n = 13, lis = [1,4,9]
        # cnt=1
        # 13
        # deque([12])
        # deque([12, 9])
        # deque([12, 9, 4])
        # 2
        # cnt=12
        # deque([9, 4, 11])
        # deque([9, 4, 11, 8])
        # deque([9, 4, 11, 8, 3])
        # 9
        # deque([4, 11, 8, 3, 8])
        # deque([4, 11, 8, 3, 8, 5])
        if n < 2:
            return n
        lis = []
        i = 1
        while i * i <= n:
            lis.append(i * i)
            i += 1
        cnt = 0
        q = collections.deque([n])
        while q:
            cnt += 1   
            size = len(q)
            for _ in range(size):
                cur_target = q.popleft()
                for candidate in lis:
                    if cur_target == candidate:
                        return cnt
                    if cur_target < candidate:
                        break
                    q.append(cur_target - candidate)
        return cnt

