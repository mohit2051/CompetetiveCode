"""
Length of Last Word
Easy
Topics
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


"""
This approach is concise and utilizes built-in string methods effectively. Here's a brief overview:

1. You use the strip() method to remove any leading or trailing whitespace from the string s.
2. Then, you use the split(' ') method to split the string into a list of words based on whitespace.
   Finally, you return the length of the last word in the list using [-1] indexing.
3. This solution is correct and efficient. It has a time complexity of O(n), where n is the length of the input string s, due to the strip() and split(' ') operations.


This solution is already quite efficient and concise. However, one potential improvement could be to avoid using the split() method, as it creates a list of all words in the string, which might be unnecessary if the string is large.

Here's an alternative approach:

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing whitespace
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Calculate the length of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length

"""
In this improved version:

1. We start from the end of the string and iterate backwards until we find the first non-space character, which is the end of the last word.
2. Then, we iterate backwards again and count the characters until we encounter a space or reach the beginning of the string.
3. This approach avoids unnecessary splitting of the string and creates less overhead, especially for large strings.

This solution still maintains a time complexity of O(n), where n is the length of the input string s, but it may perform better in practice for large inputs due to avoiding unnecessary operations.

"""