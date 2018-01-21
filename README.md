<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# Programming Homeworks for Algorithms (CMSC 37000) #

### HW1 ###

We say that a binary string B is sparse if there are no three consecutive 1’s in B. For instance, strings 1, 110101, 0001011 are sparse, but 111, 1100011100, 010101110101 are not. Given a sequence of non-negative weights $w_0, ..., w_{n−1}$, define the value of the string $B = b_0b_1...b_{n−1}$ as $\sum_{i=0}^{n-1}b_iw_i$.

Design and implement a polynomial-time algorithm that given a sequence $w'1,...,w_n$ finds the value of the most valuable spare string.

Compile: g++ -std=c++11 problem_solver.cpp -o problem_solver (GNU C++:)

Run your program: Make sure that file problem_set_0.dat is located in the same folder/directory as your executable. If your program solves all instances correctly, you will see the following message:
    
> Problem set #0. Your algorithm solved all test instances correctly. Congratulations!
    Don't forget to submit your source code and file 'solution_0.dat' via Canvas. 