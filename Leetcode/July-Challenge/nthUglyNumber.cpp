/*
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.
*/

class Solution {
public:
    int nthUglyNumber(int n) {
        int uglyN[n];
        uglyN[0] = 1;
        int count = 1;
        int idx2 = 0;
        int idx3 = 0;
        int idx5 = 0;
        
        while(count < n){
            int val2 = uglyN[idx2]*2;
            int val3 = uglyN[idx3]*3;
            int val5 = uglyN[idx5]*5;
            
            int val = min({val2, val3, val5});
            if(val==val2) {
                idx2++;
            }
            if(val==val3) {
                idx3++;
            }
            if(val==val5) {
                idx5++;
            }
            uglyN[count++] = val;
            
        }
        return uglyN[n-1];
        
    }
};
