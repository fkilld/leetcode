# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Value of the node
        self.left = left        # Left child
        self.right = right      # Right child

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Given a sorted (ascending) array, convert it to a height-balanced binary search tree (BST).
        :type nums: List[int]
        :rtype: TreeNode
        """

        # Helper function to recursively build the BST
        def buildBST(left, right):
            # If left index exceeds right, there are no elements to form a node
            if left > right:
                return None

            # Always choose the middle element to ensure balance
            mid = (left + right) // 2

            # Create a new node with the middle element
            node = TreeNode(nums[mid])

            # Recursively build the left subtree using the left half of the array
            node.left = buildBST(left, mid - 1)

            # Recursively build the right subtree using the right half of the array
            node.right = buildBST(mid + 1, right)

            # Return the constructed node
            return node

        # Start the recursion from the full array
        return buildBST(0, len(nums) - 1)

# Detailed Example:
# Input: nums = [-10, -3, 0, 5, 9]
# Step 1: mid = 2, nums[2] = 0 -> root = TreeNode(0)
# Step 2: Left subtree: nums[0:1] = [-10, -3]
#         mid = 0, nums[0] = -10 -> left child = TreeNode(-10)
#         right of -10: nums[1:1] = [-3], mid = 1, nums[1] = -3 -> right child = TreeNode(-3)
# Step 3: Right subtree: nums[3:4] = [5, 9]
#         mid = 3, nums[3] = 5 -> right child = TreeNode(5)
#         right of 5: nums[4:4] = [9], mid = 4, nums[4] = 9 -> right child = TreeNode(9)
# Final BST:
#        0
#      /   \
#   -10     5
#     \      \
#     -3      9

# Example usage and output:
def preorder_traversal(root):
    """Helper function to print tree in preorder for verification"""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    bst_root = sol.sortedArrayToBST(nums)
    print("Preorder traversal of constructed BST:", preorder_traversal(bst_root))
    # Output: Preorder traversal of constructed BST: [0, -10, -3, 5, 9]
