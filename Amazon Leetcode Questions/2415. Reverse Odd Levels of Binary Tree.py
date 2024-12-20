# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Level-order traversal using a queue
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Collect all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse values at odd levels
            if level % 2 == 1:
                left, right = 0, len(current_level) - 1
                while left < right:
                    current_level[left].val, current_level[right].val = current_level[right].val, current_level[left].val
                    left += 1
                    right -= 1
            
            level += 1
        
        return root