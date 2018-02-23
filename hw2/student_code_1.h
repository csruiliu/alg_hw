//required libraries
#include <string>
#include <iostream>
#include <math.h>
#include <string.h>
//you can include standard C++ libraries here

using namespace std;

// This function should return your name.
// The name should match your name in Canvas

void GetStudentName(std::string& your_name)
{
   //replace the placeholders "Firstname" and "Lastname"
   //with you first name and last name 
   your_name.assign("Rui Liu");
}

//This is the function you need to implement.
int ComputeOptimalTreePartition(std::vector<int> q)
{
    int vs = q.size();
    //the last number
    int vi = vs - 1;
    //possible number of sum
    int vp = 2*vs+1; 
    
    //dp table
    int** dp;

    dp = (int**)malloc(sizeof(int*)*vs);
    for(int i = 0; i < vs; i++)  
    {  
        *(dp+i) = (int*)malloc(sizeof(int)*vp);
    }  
    for(int i = 0; i < vs; ++i) {
        for(int j = 0; j < vp; ++j) {
            dp[i][j] = -1;
            //dsum[vs][vp] = 2*vs+1; 
        }
    }
    
    for(int i = vi; i >= 0; --i ) {
        //cout << "i node: " << i << endl;
        //leaf node
        if(2*i+1 > vi) {
            int tsum = q[i];
            dp[i][vs+tsum] = tsum*tsum;
        }
        //two child node
        else if(2*i+2 <= vi) {
            int left = 2*i+1;
            int right = 2*i+2;
            int tsum = q[i];
            //int sum_range = ((ht-log2(left+1))*2+1)*2;

            for(int j = 0; j < vp; ++j) {
                if(dp[left][j] != -1) {
                    int left_sum = j - vs;
                    for(int k = 0; k < vp; ++k) {
                        if(dp[right][k] != -1) {
                            int right_sum = k - vs;
                            
                            int tlrCost = dp[left][left_sum+vs] + dp[right][right_sum+vs] + tsum*tsum;
                            int tlCost = (tsum+left_sum)*(tsum+left_sum) + dp[right][right_sum+vs] + (dp[left][left_sum+vs] - left_sum*left_sum);
                            int trCost = (tsum+right_sum)*(tsum+right_sum) + dp[left][left_sum+vs] + (dp[right][right_sum+vs] - right_sum*right_sum);
                            int allCost = (tsum+right_sum+left_sum)*(tsum+right_sum+left_sum) + (dp[left][left_sum+vs] - left_sum*left_sum) + (dp[right][right_sum+vs] - right_sum*right_sum);
                            if(tlrCost > dp[i][tsum+vs]) {
                               dp[i][tsum+vs] = tlrCost; 
                            }
                            if(tlCost > dp[i][tsum+left_sum+vs]) {
                               dp[i][tsum+left_sum+vs] = tlCost; 
                            }
                            if(trCost > dp[i][tsum+right_sum+vs]) {
                               dp[i][tsum+right_sum+vs] = trCost; 
                            }
                            if(allCost > dp[i][tsum+right_sum+left_sum+vs]) {
                               dp[i][tsum+right_sum+left_sum+vs] = allCost; 
                            }
                        }
                    }
                }
            }
        }
        //one child node
        else if(2*i+1 <= vi) {
            int left = 2*i+1;
            int tsum = q[i];
            for(int j = 0; j < vp; ++j) {
                if(dp[left][j] != -1) {
                    int left_sum = j-vs;
                    int allCost = (tsum+left_sum)*(tsum+left_sum) + (dp[left][left_sum+vs] - left_sum*left_sum);
                    int tlCost = tsum*tsum + dp[left][left_sum+vs];
                    if(allCost > dp[i][tsum+left_sum+vs]) {
                        dp[i][tsum+left_sum+vs] = allCost; 
                    }
                    if(tlCost > dp[i][tsum+vs]) {
                        dp[i][tsum+vs] = tlCost; 
                    }                    
                }
            }
        }
    }
    int max = 0;

    for(int i = 0; i < vp; ++i){
        if(dp[0][i] > max) {
            max = dp[0][i];
        }
        
    }
    return max;
}



