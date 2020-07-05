'''
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  
- 1 is typically treated as an ugly number.
- n does not exceed 1690.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyN = n*[1]
        count = 1
        idx2, idx3, idx5 = 0, 0, 0
        while count < n:
            val2 = uglyN[idx2]*2
            val3 = uglyN[idx3]*3
            val5 = uglyN[idx5]*5
            val = min(val2, val3, val5)
            if val==val2:
                idx2 += 1
            if val==val3:
                idx3 += 1
            if val == val5:
                idx5 +=1
            uglyN[count] = val
            count +=1
        
        return uglyN[n-1]
