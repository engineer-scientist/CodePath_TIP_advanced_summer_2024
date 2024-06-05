'''
Problem #2: Longest Common Prefix
Problem on Leetcode: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longest_common_prefix(strings_1D):
    string_lengths_1D = []

    for s in strings_1D:
        string_lengths_1D.append(len(s))

    min_string_length_index = string_lengths_1D.index(min(string_lengths_1D))

    shortest_string = strings_1D[min_string_length_index]

    longest_common_prestring = ""
    
    for i in range(len(shortest_string)):
        counter = 0
        for s in strings_1D:
            if shortest_string[i] == s[i]:
                counter = counter + 1
            else:
                break
        if counter == len(strings_1D):
            longest_common_prestring = longest_common_prestring + shortest_string[i]
        else:
            break
    
    return longest_common_prestring


print("Enter the number of strings:")
n_strings = int(input())

strings_1D = []

for i in range(n_strings):
    print("Enter string", i + 1, ":")
    strings_1D.append(input())

print("The strings entered are: \n", strings_1D)

print("Longest common prefix is: \n", longest_common_prefix(strings_1D))
