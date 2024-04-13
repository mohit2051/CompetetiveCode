"""
28. Find the Index of the First Occurrence in a String
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if(len(needle) > len(haystack)):
            return -1
        return haystack.find(needle)

"""

This approach is straightforward and utilizes the find() method provided by Python's string objects. Here's a brief overview:

1. You first handle the case where the needle string is empty by returning 0, as an empty string is always found at index 0 in any string.
2. Then, you check if the length of the needle string is greater than the length of the haystack string. If it is, you return -1 because it's impossible for needle to be a substring of haystack.
3. Finally, you use the find() method to search for the first occurrence of the needle substring within the haystack string. If found, it returns the index of the first occurrence; otherwise, it returns -1.

This solution is correct and efficient. It has a time complexity of O(n), where n is the length of the input string haystack, due to the find() operation.

"""