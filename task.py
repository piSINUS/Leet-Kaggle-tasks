# Longest Substringf Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_index_map = {}
#         left = 0
#         max_length = 0
        
#         for right in range(len(s)):
#             if s[right] in char_index_map:
#                 left = max(left, char_index_map[s[right]] + 1)
#             char_index_map[s[right]] = right
#             max_length = max(max_length, right - left + 1)
        
#         return max_length
    

# solution = Solution()
# test = "abcabcbb"
# result = solution.lengthOfLongestSubstring(test)
# print(f"The length of the longest substring without repeating characters in '{test}' is: {result}")

# ZigZag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:  (you may want to display this pattern in a fixed font for better legibility\

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1: return s
#         a=""
#         for i in range(numRows):
#             for j in range(i,len(s),2*(numRows-1)):
#                 a+=s[j]
#                 if(i>0 and i<numRows-1 and j+2*(numRows-1)-2*i < len(s)):
#                     a+=s[j+2*(numRows-1)-2*i]
#         return a
# solution = Solution()
# test = "PAYPALISHIRING"
# numRows = 3
# result = solution.convert(test, numRows)
# print(f"The zigzag conversion of '{test}' with {numRows} rows is: {result}")

# String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        i = 0
        sign = 1
        result = 0
        if s[i] == '-' or s[i] == '+':
            sign = -1 if s[i] == '-' else 1
            i += 1
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            result = result * 10 + digit
            i += 1
        return sign * result