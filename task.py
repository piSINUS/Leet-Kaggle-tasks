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

# class Solution(object):
#     def myAtoi(self, s):
#         s = s.strip()
#         if not s:
#             return 0
#         i = 0
#         sign = 1
#         result = 0
#         if s[i] == '-' or s[i] == '+':
#             sign = -1 if s[i] == '-' else 1
#             i += 1
#         while i < len(s) and s[i].isdigit():
#             digit = int(s[i])
#             if result > (2**31 - 1 - digit) // 10:
#                 return 2**31 - 1 if sign == 1 else -2**31
#             result = result * 10 + digit
#             i += 1
#         return sign * result

# solution = Solution()
# test = "   -42"
# result = solution.myAtoi(test)
# print(f"The converted integer from '{test}' is: {result}")

#  Regular Expression Matching

# class Solution(object):
#     def isMatch(self, s: str, p:str)-> bool:
#         m, n = len(s), len(p)
#         dp = [[False] * (n + 1) for _ in range(m + 1)]
#         dp[0][0] = True
        
#         for j in range(1, n + 1):
#             if p[j - 1] == '*':
#                 dp[0][j] = dp[0][j - 2]
        
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if p[j - 1] == s[i - 1] or p[j - 1] == '.':
#                     dp[i][j] = dp[i - 1][j - 1]
#                 elif p[j - 1] == '*':
#                     dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
#         return dp[m][n]
    
# solution = Solution()
# test_s = "aab"
# test_p = ".*"
# result = solution.isMatch(test_s, test_p)
# print(f"The result of matching string '{test_s}' with pattern '{test_p}' is: {result}") 


# 11. Container With Most Water

# class Solution(object):
#     def maxArea(self, height):
#         left, right =  0, len(height) -1
#         max_area = 0 
#         while left<right:
#             width = right - left
#             current_height = min(height[left], height[right])
#             current_area = width * current_height
#             max_area = max(max_area, current_area)
            
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return max_area

# sorlution = Solution()
# test_height = [1,8,6,2,5,4,8,3,7]
# result = sorlution.maxArea(test_height)
# print(f"The maximum area of water that can be contained is: {result}")

# 12. Integer to Roman

# class Solution(object):
#     def intToRoman(self, num):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#         ]
#         syms = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#         ]
#         roman_num = ''
#         i = 0
#         while num > 0:
#             for z in range(num // val[i]):
#                 roman_num += syms[i]
#                 num -= val[i]
#             i += 1
#         return roman_num
# solution = Solution()
# test_num = 3749
# result = solution.intToRoman(test_num)
# print(f"The Roman numeral representation of {test_num} is: {result}")

# 14 Longest Common Prefix

# class Solution(object):
#     def longestCommonPrewfix(self,strs):
#         prefix= strs[0]
#         for i in range(1, len(strs)):
#              while strs[i].find(prefix) != 0:
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
#         return prefix   

# solution = Solution()
# test_strs = ["flower", "flow", "flight"]
# result = solution.longestCommonPrewfix(test_strs)
# print(f"The longest common prefix among {test_strs} is: '{result}'")

# 15. 3Sum

# class Solution(object):
#     def threeSum(self,nums):
#         nums.sort()
#         result = []
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]
#                 if total < 0:
#                     left += 1
#                 elif total > 0:
#                     right -= 1
#                 else:
#                     result.append([nums[i], nums[left], nums[right]])
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
#         return result
# solution = Solution()
# test_nums = [-1,0,1,2,-1,-4]
# result = solution.threeSum(test_nums)
# print(f"The unique triplets that sum to zero in {test_nums} are: {result}")

# 16. 3Sum Closest

# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         nums.sort()
#         closest_sum = float('inf')
        
#         for i in range(len(nums) - 2):
#             left, right = i + 1, len(nums) - 1
            
#             while left < right:
#                 current_sum = nums[i] + nums[left] + nums[right]
                
#                 if abs(current_sum - target) < abs(closest_sum - target):
#                     closest_sum = current_sum
                
#                 if current_sum < target:
#                     left += 1
#                 elif current_sum > target:
#                     right -= 1
#                 else:
#                     return current_sum
        
#         return closest_sum
# solution = Solution()
# test_nums = [-1, 2, 1, -4]
# test_target = 1
# result = solution.threeSumClosest(test_nums, test_target)
# print(f"The closest sum to {test_target} in {test_nums} is: {result}")

# 17. Letter Combinations of a Phone Number

# class Solution(object):
#     def LetterCombinations(self, digits):
#         if not digits:
#             return []
        
#         phone_map = {
#             '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
#             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
#         }
        
#         def backtrack(index, path):
#             if index == len(digits):
#                 combinations.append("".join(path))
#                 return
            
#             possible_letters = phone_map[digits[index]]
#             for letter in possible_letters:
#                 path.append(letter)
#                 backtrack(index + 1, path)
#                 path.pop()
        
#         combinations = []
#         backtrack(0, [])
#         return combinations
# solution = Solution()
# test_digits = "2"
# result = solution.LetterCombinations(test_digits)
# print(f"The letter combinations for the digits '{test_digits}' are: {result}")

# 21. Merge Two Sorted Lists
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         dummy = ListNode(0)
#         current = dummy
        
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
        
#         if list1:
#             current.next = list1
#         elif list2:
#             current.next = list2
        
#         return dummy.next
# list1= [1,2,4]
# list2 = [1,3,4]
# result = sol.mergeTwoLists(list1,list2)

# class Solution:
#     def isValid(self, s: str) -> bool:
#         mapping = {')': '(', '}': '{', ']': '['}
#         stack = []

#         for char in s:
#             if char in mapping.values():
#                 stack.append(char)
#             elif char in mapping:
#                 if not stack or mapping[char] != stack.pop():
#                     return False
#         return not stack
                
# sol = Solution()

# s = "([])"
# s1 = '(}'
# res = sol.isValid(s)
# print(res)
        
#  26 Remove Duplicates from Sorted Array

# nums = [0,0,1,1,1,2,2,3,3,4]
# class Solution(object):
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0
        
#         unique_index = 0

#         for i in range(1,len(nums)):
#             if nums[i] != nums[unique_index]:
#                 unique_index += 1
#                 nums[unique_index] = nums[i]
#         return unique_index + 1
    
# sol = Solution()
# result = sol.removeDuplicates(nums)
# print(f"The number of unique elements is: {result}")
# print(f"The modified array is: {nums[:result]}")

# 18 4SUm

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        
        return result