# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:24:07 2019

@author: lalit
"""

class Solution(object):
	def CustomSort(self, a):
		left_ptr=0
		right_ptr = len(a) - 1
		count = 0
		
		while (right_ptr > left_ptr):    
		    while(a[left_ptr] % 2 == 0):
		        left_ptr = left_ptr + 1
		        
		    while(a[right_ptr] % 2 != 0):
		        right_ptr = right_ptr - 1
		        
		    if (right_ptr > left_ptr):
		        a[left_ptr], a[right_ptr] = a[right_ptr], a[left_ptr]
		        count = count + 1
		
		print(a, "Number of Swaps ->" ,count)
		return(count)
		
if __name__ == '__main__':
	a = [6, 3, 4, 5, 11, 17, 18, 22]
	s=Solution()
	print(s.CustomSort(a))