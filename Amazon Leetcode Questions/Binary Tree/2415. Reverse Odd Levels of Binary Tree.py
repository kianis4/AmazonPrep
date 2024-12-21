# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Reverse the values of nodes at odd levels in a binary tree using level-order traversal.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            Optional[TreeNode]: The root of the modified binary tree with odd levels reversed.

        Space Complexity:
            O(N) - Space required for the queue in the worst case, where N is the total number of nodes.

        Time Complexity:
            O(N) - Each node is visited exactly once during the traversal.
        """
        
        # Initialize a queue for level-order traversal
        # The queue will help us visit nodes level by level
        queue = deque([root])
        level = 0  # Start from level 0 (root level)
        
        # Perform a level-order traversal of the binary tree
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            
            # Create a list to store the nodes at the current level
            current_level = []
            
            # Process each node in the current level
            for _ in range(level_size):
                # Remove a node from the queue
                node = queue.popleft()
                # Add the node to the current level list
                current_level.append(node)
                
                # Add the left and right children (if they exist) to the queue
                # for processing in the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Check if the current level is odd
            if level % 2 == 1:
                # If it is, reverse the values of the nodes at this level
                # Use two pointers to swap values from both ends of the list
                left, right = 0, len(current_level) - 1
                while left < right:
                    # Swap the values of nodes at indices `left` and `right`
                    current_level[left].val, current_level[right].val = (
                        current_level[right].val,
                        current_level[left].val,
                    )
                    # Move the pointers closer to the center
                    left += 1
                    right -= 1
            
            # Increment the level counter to move to the next level
            level += 1
        
        # Return the modified root of the binary tree
        return root