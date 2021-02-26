//you can include standard C++ libraries here

//required libraries
#include <vector>

using namespace std;
// This function should return your name.
// The name should match your name in Canvas

void GetStudentName(std::string& your_name)
{
   your_name.assign("Rui Liu");
}

//This is the function you need to implement.
int FindMaximumProfit(std::vector<int> w)
{
    int n = w.size();
    int sw[n];

    sw[0] = w[0];
    sw[1] = w[0] + w[1];
    sw[2] = max(max(w[1] + w[2], w[0] + w[2]), sw[1]);
    for (int i = 3; i < n; ++i) {
        sw[i] = max(max(w[i] + w[i-1] + sw[i-3], sw[i-2] + w[i]), sw[i-1]);
    }

    return sw[n-1];
}


