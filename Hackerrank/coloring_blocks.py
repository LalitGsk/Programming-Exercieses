'''Color the Blocks/Paint House type : Given the cost of using each color on each block, determine the minimum cost to color all of the Blocks.
 (No two adjacent blocks can be the same color.)
 input e.g. [[1,2,3][1,2,3][3,3,1]]
 '''

def minPrice(cost):
    if(costs==null||costs.length==0)
        return 0;
 
    for(int i=1; i<costs.length; i++){
        costs[i][0] += Math.min(costs[i-1][1], costs[i-1][2]);
        costs[i][1] += Math.min(costs[i-1][0], costs[i-1][2]);
        costs[i][2] += Math.min(costs[i-1][0], costs[i-1][1]);
    }
 
    int m = costs.length-1;
    return Math.min(Math.min(costs[m][0], costs[m][1]), costs[m][2]);
