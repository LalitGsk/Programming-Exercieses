'''
Funtion returns the final number of instances running.
25% <= avg_util <= 60 or avg_util=1 : no action
avg_util > 60: double instances and stop polling for 10s
avg_util < 25: halve instances and stop polling
input e.g - [25,23,1,2,3,4,5,6,7,8,9,10,76,80] output: 2
'''
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'finalInstances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER instances
#  2. INTEGER_ARRAY averageUtil
#
import math
def finalInstances(instances, averageUtil):
    # Write your code here
    
    left = 0
    
    while(left < len(averageUtil)):

        current = averageUtil[left]
        if current >= 25 and current <= 60:
            left = left + 1

        elif(current < 25):
            if(instances>1):
                instances = instances/2
                instances = math.ceil(instances)
                left = left+11
            else:
                left = left + 1
        else:
            temp = instances*2
            if temp < (2*(10**8)):
                instances = temp
                left = left+11
            else:
                left = left + 1    
    return(instances)