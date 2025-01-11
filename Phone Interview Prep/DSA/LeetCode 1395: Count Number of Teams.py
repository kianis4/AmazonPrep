# LeetCode 1395: Count Number of Teams
# You are given an array `rating` of soldiers' ratings. You must form teams of 3 soldiers such that:
# 1. The ratings of the team satisfy either:
#    - (rating[i] < rating[j] < rating[k]) (increasing order)
#    - (rating[i] > rating[j] > rating[k]) (decreasing order)
# 2. The indices satisfy: 0 <= i < j < k < len(rating).
#
# Return the number of valid teams that can be formed.
#
# Constraints:
# - 3 <= len(rating) <= 1000
# - 1 <= rating[i] <= 10^5 (all ratings are unique).
#
# Example:
# Input: rating = [2, 5, 3, 4, 1]
# Output: 3
# Explanation: Valid teams are:
#   - (2, 3, 4)
#   - (5, 4, 1)
#   - (5, 3, 1)
#
# Runtime Complexity: O(n^2) - for each soldier (middle index j), we count possible teams using two linear passes.
# Space Complexity: O(1) - only integer counters are used for computation.

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0  # Initialize count of valid teams
        
        # Iterate through the array, treating each soldier as the "middle" soldier
        for j in range(1, len(rating) - 1):
            middleSoldier = rating[j]
            
            # Initialize counters
            leftLess = leftGreater = 0
            rightLess = rightGreater = 0
            
            # Count soldiers to the left of j
            for l in range(j):
                if rating[l] < middleSoldier:
                    leftLess += 1
                elif rating[l] > middleSoldier:
                    leftGreater += 1
            
            # Count soldiers to the right of j
            for r in range(j + 1, len(rating)):
                if rating[r] < middleSoldier:
                    rightLess += 1
                elif rating[r] > middleSoldier:
                    rightGreater += 1
            
            # Calculate the number of valid teams with j as the middle soldier
            res += (leftLess * rightGreater) + (leftGreater * rightLess)
        
        return res

# Example usage:
# solution = Solution()
# print(solution.numTeams([2, 5, 3, 4, 1])) # Output: 3