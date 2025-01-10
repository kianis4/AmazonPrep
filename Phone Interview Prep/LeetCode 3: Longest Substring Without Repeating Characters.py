# LeetCode 3: Longest Substring Without Repeating Characters
# Given a string `s`, find the length of the longest substring without repeating characters.
#
# Constraints:
# - 0 <= s.length <= 5 * 10^4
# - s consists of English letters, digits, symbols, and spaces.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. Note that "pwke" is not a substring.
#
# Approach:
# - Use a sliding window approach with two pointers (`l` and `r`) to track the current substring.
# - Use a dictionary to keep track of characters in the current substring.
# - When a repeating character is encountered, move the left pointer (`l`) to remove it.
#
# Runtime Complexity: O(n), where n is the length of the string. Each character is visited at most twice.
# Space Complexity: O(min(n, |Σ|)), where Σ is the character set (e.g., 26 for lowercase English letters).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize pointers and the data structures
        l, r = 0, 0  # Sliding window pointers
        seen = {}    # Dictionary to store characters in the current window
        res = 0      # Maximum length of substring without repeating characters
        
        # Expand the right pointer (r) until we traverse the entire string
        while r < len(s):
            if s[r] in seen:
                # Update the result before fixing the repeat
                res = max(res, len(s[l:r]))
                
                # Move the left pointer (l) until the duplicate is removed
                while s[r] in seen:
                    del seen[s[l]]
                    l += 1

            # Add the current character to the seen dictionary
            seen[s[r]] = 1
            r += 1  # Move the right pointer

        # Ensure the last substring is considered
        return max(res, len(s[l:r]))

# Example usage:
# solution = Solution()
# print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3