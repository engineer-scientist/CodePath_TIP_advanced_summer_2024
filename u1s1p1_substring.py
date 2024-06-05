'''
Problem #1: Substring

Write a function that takes in two strings and returns True if the second string is a substring of the first, and False otherwise.

NOTE: You may not use the in operator (Python) or call a library function that tests for substrings, such as substring() or indexOf() (Java).

Example 1:
Input: laboratory, rat
Output: true

Example 2:
Input: cat, meow
Output: false
'''

def substring(str1, str2):
  if len(str2) > len(str1):
    return False
  for i in range(len(str1)):
    if str1[i] == str2[0]:
      if str1[i : i + len(str2)] == str2:
        return True
  return False

print("Enter the first string:")
str1 = input()

print("\n Enter the second string:")
str2 = input()

if substring(str1, str2):
  print("\n True: The second string (", str2, ") is a part of the first string (", str1, ").")
else:
  print("\n False: The second string (", str2, ") is not a part of the first string (", str1, ").")
