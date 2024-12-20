class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        currMax = max(candies)


        for idx, child in enumerate(candies):
            if child + extraCandies >= currMax:
                candies[idx] = True
            else:
                candies[idx] = False
        return candies