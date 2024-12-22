class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
        Calculate the minimum number of swaps required to group all 1s together in a binary array.

        Space Complexity:
            O(1) - We use a few variables (pointers, sums) that do not depend on the size of the input.
        
        Time Complexity:
            O(n) - The sliding window traverses the array once, making the solution linear in the input size.

        Args:
            data (List[int]): A list of binary integers (0s and 1s).

        Returns:
            int: The minimum number of swaps needed to group all 1s together.
        """
        # Step 1: Count the total number of 1s in the array
        amount = sum(data)  # O(n) time complexity
        
        # If there are no 1s or only one 1, no swaps are needed
        if amount <= 1:
            return 0

        # Step 2: Initialize sliding window
        l, currSum, maxOnesInWindow = 0, 0, 0
        
        # Step 3: Slide the window across the array
        for r in range(len(data)):  # O(n) time complexity
            # Add the rightmost element to the current sum
            currSum += data[r]
            
            # Maintain the window size equal to `amount`
            if r - l + 1 > amount:
                currSum -= data[l]  # Remove the leftmost element
                l += 1  # Slide the left pointer
            
            # Track the maximum number of 1s in the current window
            maxOnesInWindow = max(maxOnesInWindow, currSum)
        
        # Step 4: Calculate the minimum swaps
        return amount - maxOnesInWindow