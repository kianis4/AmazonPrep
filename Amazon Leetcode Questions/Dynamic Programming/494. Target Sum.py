class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Returns the number of ways to assign '+' or '-' to each element in nums so 
        that the resulting expression sums up to 'target'.
        
        Approach:
        1. Compute S = sum(nums).
        2. Because we want: (sum of +subset) - (sum of -subset) = target,
        we derive:  2 * (sum of +subset) = S + target  =>  P = (S + target) // 2.
        - If (S + target) is negative or odd, we cannot form such P. Return 0.
        3. Now the problem reduces to counting how many subsets of nums sum to P.
        4. Use a 1-D dp array (size P+1) where dp[j] is the number of ways to form sum j.
        - Initialize dp[0] = 1, meaning there's exactly 1 way to form sum 0 
            (by choosing no elements).
        - For each num in nums, update dp in reverse (from P down to num) to 
            avoid counting the same item more than once in a single iteration.
        5. Finally, dp[P] gives the number of ways to form sum P.

        Time Complexity: O(n * P), where n = len(nums) and P = (S + target) // 2.
        Space Complexity: O(P), since we use a 1-D dp array of length P+1.
        """
        S = sum(nums)
        
        # If S + target is negative or odd, it's impossible to find a valid P.
        if (S + target) < 0 or (S + target) % 2 != 0:
            return 0
        
        P = (S + target) // 2

        # dp[j] = number of ways to form sum j with elements in nums
        dp = [0] * (P + 1)
        dp[0] = 1  # There's exactly one way to make sum 0: choose no elements

        # Build the dp array using each num in nums
        for num in nums:
            # Update in descending order to avoid double counting
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[P]