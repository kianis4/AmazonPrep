# LeetCode 116: Populating Next Right Pointers in Each Node
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Constraints:
# - The number of nodes is in the range [0, 2^12 - 1].
# - -1000 <= Node.val <= 1000
#
# Follow-up:
# - You may only use constant extra space.
# - Recursive approach is fine. Assume implicit stack space does not count as extra space.
#
# Example:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: The binary tree looks like this:
#        1 -> NULL
#      /   \
#     2  -> 3 -> NULL
#    / \    / \
#   4-> 5->6-> 7 -> NULL
#
# Approach:
# - Use BFS with a queue to traverse the tree level by level.
# - At each level, connect nodes to their right neighbor and set the last node's `next` pointer to NULL.
#
# Runtime Complexity: O(n), where n is the number of nodes in the tree (each node is visited once).
# Space Complexity: O(n) for the queue used in BFS.

from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # If the root is empty, return None
        if not root:
            return None
        
        # Initialize a queue for BFS
        queue = deque([(root, 1)])  # Store nodes with their level information
        
        while queue:
            # Pop the front node and its level from the queue
            node, level = queue.popleft()
            
            # If there is a next node in the queue and it is on the same level,
            # set the current node's next pointer to that node
            if queue and queue[0][1] == level:
                node.next = queue[0][0]
            else:
                # Otherwise, set the next pointer to None
                node.next = None
            
            # Add the children of the current node to the queue
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return root

# Example usage:
# root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
# solution = Solution()
# solution.connect(root)