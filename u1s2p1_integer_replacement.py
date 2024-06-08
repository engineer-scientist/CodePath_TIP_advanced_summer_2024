'''
Problem 1: Integer Replacement
Problem on Leetcode: Integer Replacement
Given a positive integer n, you can apply one of the following operations:
If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.
Tip: Java programmers should treat Integer.MAX_VALUE() as a special case.

Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1.

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1.

Example 3:
Input: n = 4
Output: 2
Explanation: 4 -> 2 -> 1.
'''

n_operations = 0

print("Given a positive integer n, we will reduce it to 1 by applying the following operations:")
print("If n is even, then it will be replaced with n / 2.")
print("If n is odd, then it will be replaced with n - 1.")
print("The minimum number of operations (needed for n to become 1) will be displayed. \n")

print("Please enter n (must be a positive integer):")
n = int(input())
while (n <= 0):
    print(n, "is not a positive integer. Please enter a positive integer:")
    n = int(input())

while (n > 1):
    if (n % 2) == 0:
        n = n / 2
    else:
        n = n - 1
    n_operations = n_operations + 1

print("The minimum number of operations needed to reduce n to 1 is", n_operations, ".")
