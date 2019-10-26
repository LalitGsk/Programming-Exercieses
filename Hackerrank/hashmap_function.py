# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:23:47 2019

@author: lalit
"""

def hashmap(queryType, query):
	keys=[]
	val=[]
	result_get=0
	for qt, q in zip(queryType, query):
		if qt=="insert":
			keys.append(q[0])
			val.append(q[1])
		elif qt=="addToValue":
			for i in range(len(val)):
				val[i]+=q[0]
		elif qt=="addToKey":
			for i in range(len(keys)):
				keys[i]+=q[0]
		elif qt=="get":
			result_get+=val[keys.index(q[0])]
			
	return result_get

#queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
#query = [[1,2],[2,3], [2], [1], [3]]


queryType= ["addToKey", "addToValue", "insert", "addToValue", "insert", "insert", "addToKey", "addToValue","insert", "get", "addToKey", "insert", "get", "get", "get", "get", "insert", "addToValue", "insert", "insert", "addToKey", "addToKey", "addToKey", "get", "insert", "insert", "insert", "addToValue", "insert", "addToKey", "addToValue", "addToKey", "get", "get", "addToKey", "get", "get", "addToValue", "addToKey", "addToKey", "get", "addToValue", "addToValue", "addToKey", "addToValue", "get", "get", "get", "addToValue", "addToValue", "get", "addToValue", "addToValue", "addToKey", "insert", "insert", "get", "get", "addToKey", "get", "get", "addToKey", "addToValue", "addToKey", "addToValue", "insert", "get", "insert", "addToValue", "get", "insert", "insert", "addToKey", "addToValue", "insert", "insert", "insert", "get", "get", "addToValue", "insert", "get", "addToKey", "addToKey", "addToKey", "addToKey", "addToValue", "insert", "addToValue", "get", "addToKey", "addToValue", "get", "get", "addToValue", "addToKey", "get", "addToKey", "addToKey", "addToKey"]

query= [[-5], [23], [-17,23], [30], [45,11], [25,37], [-40], [-36], [26,-22], [-15], [16],  [24,-37], [24], [21], [-41], [-41], [19,38], [-34], [7,41], [37,39], [0], [17], [-27], [27], [-1,3], [8,7], [6,22], [5], [49,20], [46], [-29], [35], [90], [30], [7], [115], [85], [-49], [-30], [43], [98], [-6], [24], [-12], [-40], [116], [121], [103], [39], [49], [95], [16], [-37], [25], [44,-50], [-29,42], [128], [44], [3], [166], [126], [24], [27], [-2], [-3], [24,-24], [150], [38,-34], [-35], [150], [8,-32], [14,16], [-6], [-9], [-35,37], [-34,43], [-45,2], [147], [124], [27], [-44,-29], [-35], [5], [5], [-17], [11], [19], [-23,-33],[48], [146], [-38], [14], [-79], [90], [-11], [-7], [-75], [-32], [0], [45]]

print(hashmap(queryType, query))
		