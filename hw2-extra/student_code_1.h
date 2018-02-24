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

    int ht = log2(vs);
    
    //dp table
    int** dp;

    int htb[ht+1];
    htb[0] = 1;
    for(int i = 1; i <= ht+1; ++i) {
        htb[i] = htb[i-1] * 2 +1;
    }
    
    dp = (int**)malloc(sizeof(int*)*vs);
    
    for(int i = vi; i >= 0; --i ) {
        //leaf node
        if(2*i+1 > vi) {
            
            int tsum = q[i];
            int lgix = log2(i+1);
            int idx = ht - lgix;
            int par = htb[idx];
            int parm = htb[idx+1];
            *(dp+i) = (int*)malloc(sizeof(int)*parm);
            for(int j = 0; j < parm; ++j) {
                dp[i][j] = -1; 
            }
            dp[i][tsum+par] = tsum*tsum;
        }
        //two child node
        else if(2*i+2 <= vi) {
            int lgix = log2(i+1);
            int idx = ht - lgix;
        
            int par = htb[idx];
            int parp = htb[idx-1];
            int parm = htb[idx+1];
             *(dp+i) = (int*)malloc(sizeof(int)*parm);
            int left = 2*i+1;
            int right = 2*i+2;
            int tsum = q[i];
            
            for(int j = 0; j < parm; ++j) {
                dp[i][j] = -1; 
            }
            
            for(int j = 0; j < par; ++j) {
                if(dp[left][j] != -1) {
                    int left_sum = j - parp;
                    for(int k = 0; k < par; ++k) {
                        if(dp[right][k] != -1) {
                            int right_sum = k - parp;
                             
                            int tlrCost = dp[left][left_sum+parp] + dp[right][right_sum+parp] + tsum*tsum;
                            int tlCost = (tsum+left_sum)*(tsum+left_sum) + dp[right][right_sum+parp] + (dp[left][left_sum+parp] - left_sum*left_sum);
                            int trCost = (tsum+right_sum)*(tsum+right_sum) + dp[left][left_sum+parp] + (dp[right][right_sum+parp] - right_sum*right_sum);
                            int allCost = (tsum+right_sum+left_sum)*(tsum+right_sum+left_sum) + (dp[left][left_sum+parp] - left_sum*left_sum) + (dp[right][right_sum+parp] - right_sum*right_sum);
                            if(tlrCost > dp[i][tsum+par]) {
                                dp[i][tsum+par] = tlrCost; 
                            }
                            if(tlCost > dp[i][tsum+left_sum+par]) {
                                dp[i][tsum+left_sum+par] = tlCost; 
                            }
                            if(trCost > dp[i][tsum+right_sum+par]) {
                                dp[i][tsum+right_sum+par] = trCost; 
                            }
                            if(allCost > dp[i][tsum+right_sum+left_sum+par]) {
                                dp[i][tsum+right_sum+left_sum+par] = allCost; 
                            }
                        }
                    }
                }
            }
            free(*(dp+left));
            free(*(dp+right));
            

        }
        //one child node
        else if(2*i+1 <= vi) {
            int lgix = log2(i+1);
            int idx = ht - lgix;
        
            int par = htb[idx];
            int parp = htb[idx-1];
            int parm = htb[idx+1];
            *(dp+i) = (int*)malloc(sizeof(int)*parm);

            int left = 2*i+1;
            int tsum = q[i];
            //*(dp+i) = (int*)malloc(sizeof(int)*vp);
            for(int j = 0; j < parm; ++j) {
                dp[i][j] = -1; 
            }
            for(int j = 0; j < par; ++j) {
                if(dp[left][j] != -1) {
                    int left_sum = j-parp;
                    int allCost = (tsum+left_sum)*(tsum+left_sum) + (dp[left][left_sum+parp] - left_sum*left_sum);
                    int tlCost = tsum*tsum + dp[left][left_sum+parp];
                    if(allCost > dp[i][tsum+left_sum+par]) {
                        dp[i][tsum+left_sum+par] = allCost; 
                    }
                    if(tlCost > dp[i][tsum+par]) {
                        dp[i][tsum+par] = tlCost; 
                    }                    
                }
            }
            free(*(dp+left));
        }
    }
    int max = 0;
    int bound = htb[ht+1];
    for(int i = 0; i < bound; ++i){
        if(dp[0][i] > max) {
            max = dp[0][i];
        }
    }
    
    return max;
}



