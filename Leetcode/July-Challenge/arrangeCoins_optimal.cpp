// Given n, find the total number of full staircase rows that can be formed. n is a non-negative integer and fits within the range of a 32-bit signed integer.
/* Example 1:  
n = 5  
The coins can form the following rows:  
¤  
¤ ¤  
¤ ¤  
Because the 3rd row is incomplete, we return 2.  
*/  

//Optimal Solution
class Solution {
public:
    int arrangeCoins(int n) 
    {
        long long lo=0,hi=100000,mid,ans=0;
        while(lo<=hi)
        {
            mid=(lo+hi)/2;
            long long x=(mid*(mid+1))/2;
            if(x<=n)
            {
                ans=mid;
                lo=mid+1;
            }
            else hi=mid-1;
        }
        return ans;
    }
};
