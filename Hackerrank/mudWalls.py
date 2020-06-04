"""
Created on Sat Mar 28 11:58:38 2020

@author: lalit
"""
import math
def mudWalls(wP, wH):
	res = {}
	ans=[]
	wH_i=0
	for i in range(1, max(wP)+1):
		if i in wP:
			print(str(i) + ' if')
			res[i] = wH[wH_i]
			wH_i +=1
		else:
			print(str(i) + " else")
			print(res[wH_i], ' ', wH[wH_i])
			res[i] = math.ceil((res[i-1] + wH[wH_i])/2)
			ans.append(res[i])
		print("wH_i ", wH_i)
		print(res)
			
	return max(ans)

wP = [1,3,7]
wH = [4,3,3]
print(mudWalls(wP, wH))
		