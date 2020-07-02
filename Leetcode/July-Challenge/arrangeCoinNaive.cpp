// Given n, find the total number of full staircase rows that can be formed. n is a non-negative integer and fits within the range of a 32-bit signed integer.
/* Example 1:  
n = 5  
The coins can form the following rows:  
¤  
¤ ¤  
¤ ¤  
Because the 3rd row is incomplete, we return 2.  
*/  

//Naive Solution
class Solution {
public:
    int arrangeCoins(int n) {
        int i=1;
        while(i<=n){
            n=n-i;
            i=i+1;
                
        }
        return (i-1);
    }
};

