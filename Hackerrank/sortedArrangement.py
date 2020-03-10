# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:45:31 2020

@author: lalit
"""

def sorted_Arrangement(a):
	
	res =[]
	count =0
	if not res:
			res.append(a[0])
			#res.sort()
			count+=1
			print('array ', res)
	for i in range(1,len(a)):
		curr = a[i]
		
		if curr <= min(res) or curr >= max(res):
			res.append(curr)
			res.sort()
			count+= 1
			print('array2 ',res)
			continue
		
		res.append(curr)
		res.sort()
		pos = res.index(curr)
		print('pos ', pos)
		print('array ', res)
		print('min ',min(pos - 0, len(res)-pos-1))
		if res[pos] == res[pos+1] and (pos - 0)>=(len(res)-pos-1):
			cnt= res.count(res[pos])-1
			count += min(pos - 0, len(res)-pos-1 - cnt)*2 +1
			continue
		count += min(pos - 0, len(res)-pos-1)*2 +1
		print('count ', count)
		
	return count

		
def getPosition(num, arr):
	if num < min(arr) or num > max(arr):
		return 0
	mid = len(arr)//2
	left = 0
	right = len(arr)-1
	while left < right:
			
		if num < arr[mid]:
			right = mid-1
		elif num > arr[mid]:
			left = mid
		else:
			break
		mid = (left+right)//2
	return mid

#ar = [10, 6,2,3,7,1,2]
ar = [2,1,6,13,6,6,15,13]
#ar = [9,8,4,9,28,21,24,18,29,25,9,3,19,5,3]
#ar = [2,19,10,1,6,13,6,6,15,12]
#ar = [790,851,728,113,844,982,769,372,165,663,734,879,652,573,848,717,593,508,124,496,858,1,793,32,474,617,817,562,612,515,783,844,792,938,757,537,726,419,957,507,609,879,867,206]
print(sorted_Arrangement(ar))