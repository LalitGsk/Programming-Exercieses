# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:23:10 2020

@author: lalit
"""

def sortedArrange(numbers):
	
	#output = []
	operations =1
	
	
	
	for i in range(1,len(numbers)):
		tmp = sorted(numbers[:i+1]).index(numbers[i])
		print('pos ',tmp)
		print(sorted(numbers[:i+1]))
		
		print(numbers[i],' count ',sorted(numbers[:i+1]).count(numbers[i]))
		
		print(len(numbers[:i+1])-1-tmp)
		cnt = sorted(numbers[:i+1]).count(numbers[i])-1
		#if numbers[:i+1].count(numbers[i]) > 1 and (tmp-0 >= len(numbers[:i+1])-1-tmp-cnt):	
			
		operations += min(tmp-0,len(numbers[:i+1])-1-tmp-cnt)*2 + 1
		print('repeating')
		#else:
		#	operations += min(tmp-0,len(numbers[:i+1])-tmp-1)*2 + 1
		print('distinct')
		print('oper ',operations)
		
		
	return operations

ar = [2,1,6,13,6,6,15,13]
#ar = [10, 6,2,3,7,1,2]
#ar = [2,19,10,1,6,13,6,6,15,12]
print(sortedArrange(ar))