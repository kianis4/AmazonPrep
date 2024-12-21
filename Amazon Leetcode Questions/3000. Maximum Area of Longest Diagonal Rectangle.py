class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """
        Finds the area of the rectangle with the largest diagonal among a list of rectangles.
        If two rectangles have the same diagonal, returns the one with the largest area.

        Args:
            dimensions (List[List[int]]): A list of rectangles, where each rectangle is represented 
                                        as [width, height].

        Returns:
            int: The area of the rectangle with the largest diagonal or largest area in case of ties.

        Space Complexity:
            O(1) - Constant space usage for variables.
        Time Complexity:
            O(N) - Iterates through the list of rectangles once.
        """

        # Initialize variables to track the largest diagonal and resulting area
        largestHypot = float("-inf")  # Keeps track of the largest diagonal found so far
        res = 0  # Stores the area of the rectangle with the largest diagonal

        # Iterate through each rectangle in the dimensions list
        for rect in dimensions:
            # Calculate the area of the current rectangle
            currArea = rect[0] * rect[1]
            
            # Calculate the diagonal (hypotenuse) of the current rectangle
            # Formula: sqrt(width^2 + height^2)
            hypotnuse = sqrt(rect[0]**2 + rect[1]**2)

            # Check if the current diagonal is larger than the largest found so far
            if hypotnuse > largestHypot:
                # Update the result area and the largest diagonal
                res = currArea
                largestHypot = hypotnuse
            elif hypotnuse == largestHypot:
                # If the diagonals are equal, update the result to the larger area
                res = max(currArea, res)

        # Return the area of the rectangle with the largest diagonal
        return res
        