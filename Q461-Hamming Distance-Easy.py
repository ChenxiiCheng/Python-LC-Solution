'''
Question: 
  461. Hamming Distance

Descrition: 
   The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
   Given two integers x and y, calculate the Hamming distance.
   
   Note:
	    0 ≤ x, y < 231.

Example:

	Input: x = 1, y = 4

	Output: 2

	Explanation:
	1   (0 0 0 1)
	4   (0 1 0 0)
	       ↑   ↑

	The above arrows point to positions where the corresponding bits are different.
'''

#Python code

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #Solution 2
        return bin(x ^ y).count('1')
        
        
        #Solution
        #print(type(x ^ y)) -> int
        z = x ^ y
        count = 0
        while(z):
            count = count + z % 2
            z = z // 2
        return count

        