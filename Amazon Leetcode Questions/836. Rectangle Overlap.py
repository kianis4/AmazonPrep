class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        Determine if two rectangles overlap.

        Args:
            rec1 (List[int]): Coordinates of the first rectangle [x1, y1, x2, y2].
            rec2 (List[int]): Coordinates of the second rectangle [x1, y1, x2, y2].

        Returns:
            bool: True if the rectangles overlap, False otherwise.

        Space Complexity:
            O(1) - Constant space used for variables.
        Time Complexity:
            O(1) - Constant time as we only perform comparisons and logical checks.
        """

        # Extract the x and y ranges for both rectangles
        # Each range is represented as [left, right] for x and [bottom, top] for y
        x1_range, y1_range = [rec1[0], rec1[2]], [rec1[1], rec1[3]]
        x2_range, y2_range = [rec2[0], rec2[2]], [rec2[1], rec2[3]]

        # Check if there is any overlap in the x-range between the two rectangles
        # Case 1: The left edge of rectangle 2 is within the x-range of rectangle 1
        xInterceptsLeftCorner = x1_range[0] < x2_range[0] < x1_range[1] or x2_range[0] < x1_range[0] < x2_range[1]
        
        # Case 2: The right edge of rectangle 2 is within the x-range of rectangle 1
        xInterceptsRightCorner = x1_range[0] < x2_range[1] < x1_range[1] or x2_range[0] < x1_range[1] < x2_range[1]
        
        # Combine both cases to determine overall x-range overlap
        xIntercepts = xInterceptsLeftCorner or xInterceptsRightCorner

        # Check if there is any overlap in the y-range between the two rectangles
        # Case 1: The bottom edge of rectangle 2 is within the y-range of rectangle 1
        yInterceptsLeftCorner = y1_range[0] < y2_range[0] < y1_range[1] or y2_range[0] < y1_range[0] < y2_range[1]
        
        # Case 2: The top edge of rectangle 2 is within the y-range of rectangle 1
        yInterceptsRightCorner = y1_range[0] < y2_range[1] < y1_range[1] or y2_range[0] < y1_range[1] < y2_range[1]
        
        # Combine both cases to determine overall y-range overlap
        yIntercepts = yInterceptsLeftCorner or yInterceptsRightCorner

        # Both x and y ranges must overlap for the rectangles to intersect
        if xIntercepts and yIntercepts:
            return True
        # If either x or y range does not overlap, the rectangles do not intersect
        else:
            return False