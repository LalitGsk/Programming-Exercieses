'''Color the Blocks/Paint House type : Given the cost of using each color on each block, determine the minimum cost to color all of the Blocks.
 (No two adjacent blocks can be the same color.)
 input e.g. [[1,2,3][1,2,3][3,3,1]]
 '''

def minCost(costs):
    if(costs==None or len(costs)==0):
        return 0;
 
    for i in range(1, len(costs)):
        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][0], costs[i-1][1])
 
    m = costs.length-1
    return min(min(costs[m][0], costs[m][1]), costs[m][2])
