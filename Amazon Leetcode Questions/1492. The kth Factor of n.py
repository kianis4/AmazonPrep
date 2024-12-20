class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Initialize an empty list to store factors of 'n'
        res = []
        
        # Iterate through all numbers from 1 to 'n' (inclusive)
        # Time Complexity: O(n) - We iterate through all numbers from 1 to 'n'
        for val in range(1, n + 1):
            # Check if 'val' is a factor of 'n' (no remainder when dividing 'n' by 'val')
            if n % val == 0:
                res.append(val)  # Append the factor to the result list
                # Space Complexity: O(d) - At most 'd' factors can be stored in 'res'
        
        # Return the k-th factor if it exists, else return -1
        # 'k-1' is used because list indices start at 0
        # Time Complexity for this operation: O(1) - Accessing an element in a list is constant time
        # Final Runtime: O(n) + O(1) = O(n)
        # Final Space Complexity: O(d)
        return res[k - 1] if len(res) >= k else -1