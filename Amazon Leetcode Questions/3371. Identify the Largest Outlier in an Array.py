class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # Calculate the sum of all elements in the list
        total_sum = sum(nums)  # O(n) time to calculate sum
        
        # Dictionary to count the frequency of each number in the list
        # defaultdict is used to avoid KeyError during increment
        num_counts = defaultdict(int)  # Space: O(k), where k is the number of unique elements in nums
        
        for num in nums:  # O(n) time to iterate over nums
            num_counts[num] += 1
        
        # Initialize largest_outlier to negative infinity to find the maximum outlier
        largest_outlier = float('-inf')
        
        # Iterate over each unique number in num_counts
        for num in num_counts.keys():  # O(k), where k is the number of unique elements in nums
            # Calculate the potential outlier based on the formula
            # potential_outlier = total_sum - 2 * num
            # This equation comes from balancing the list such that the sum excluding 'num' matches 'num'.
            potential_outlier = total_sum - 2 * num  
            
            # Check if the potential outlier exists in num_counts
            if potential_outlier in num_counts:
                # Ensure that if potential_outlier equals num, there are at least two occurrences
                if potential_outlier != num or num_counts[num] > 1:
                    # Update the largest outlier if this one is larger
                    largest_outlier = max(largest_outlier, potential_outlier)
        
        # Return the largest valid outlier found, or negative infinity if none exist
        return largest_outlier