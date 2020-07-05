''' The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
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
The above arrows point to positions where the corresponding bits are different. '''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
      L = max(len(bin(x)[2:]),len(bin(y)[2:]))
      bin_x = bin(x)[2:].zfill(L)
      bin_y = bin(y)[2:].zfill(L)
      result=0
      #print(bin_x, bin_y)
      for i in range(len(bin_x)):
          if bin_x[i]!=bin_y[i]:
              result+=1
      return result"""
        
