import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        Find the dimensions of a rectangle (length and width) such that:
        1. The rectangle's area equals the given `area`.
        2. The difference between the length and width is minimized.
        
        Args:
            area (int): The area of the rectangle.

        Returns:
            List[int]: The dimensions [length, width], where length >= width.

        Space Complexity:
            O(1) - Constant space usage for variables.
        Time Complexity:
            O(sqrt(N)) - Starts at the square root and checks divisors down to 1.
        """
        
        # Start with the largest possible width that minimizes the difference
        # Take the integer square root of the area to get the initial width (w)
        w = int(math.sqrt(area))
        
        # Iterate to find the largest width (w) that divides the area evenly
        # The loop runs until we find a divisor of `area`
        while area % w != 0:
            w -= 1  # Decrement width until a valid divisor is found
        
        # Calculate the corresponding length (l) such that l * w = area
        l = area // w  # Division gives the length for the current width
        
        # Return the dimensions [length, width]
        return [l, w]