# Definition for a binary tree node.
class TreeNode(object):

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def printTree(node, level=0):
  if node != None:
    printTree(node.right, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printTree(node.left, level + 1)


def array_to_binary_tree(arr):
  if not arr:
    return None

  root = TreeNode(arr[0])
  queue = [root]
  i = 1

  while queue and i < len(arr):
    node = queue.pop(0)  # popping off first elem

    if i < len(arr):
      if arr[i] is not None:
        node.left = TreeNode(arr[i])
        queue.append(node.left)
      i += 1

    if i < len(arr):
      if arr[i] is not None:
        node.right = TreeNode(arr[i])
        queue.append(node.right)
      i += 1

  return root


# leetcode array representation of tree
# 
# [2,1,3]
# 
#     -> 3
# -> 2
#     -> 1
# 
# [4,2,7,1,3,6,9]
# 
#         -> 9
#     -> 7
#         -> 6
# -> 4
#         -> 3
#     -> 2
#         -> 1
# 
# [4,2,7,1,3,6,9,1,2,3,4,5,6,7,8]
# 
#         -> 9
#     -> 7
#         -> 6
# -> 4
#         -> 3
#     -> 2
#         -> 1

# invert treeeeeeeeeeeeeeeeeee
#
#         /\
#  |\    /  \    /|
#  | \   \  /   / |
#  |  |  \  /  |  |
#   \  \ \  / /  /
# |\__\ \\  // /__/|
#  \___--    --___/
#      /_/||\_\
#         ||
#
# https://leetcode.com/problems/invert-binary-tree/description/


def invertTree(root):
  """
    :type root: TreeNode
    :rtype: TreeNode
    """

  def dfs(root):
    if not root:
      return None

    print("\nsublevel\n")
    printTree(root)

    dfs(root.right)
    dfs(root.left)

    root.left, root.right = root.right, root.left
    if root.right or root.left:
      print("\nAFTER-SWAP\n")
      printTree(root)

  dfs(root)
  return root


# arr = [4,2,7,1,3,6,9,1,2,3,4,5,6,7,8]
# tree = array_to_binary_tree(arr)
# # print("inverted tree")
# # invert = invertTree(tree)
# printTree(tree)


# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#[2,1,3] # [1, None, 2]
def betterMaxDepth(root):
  def dfs(root, count):
      if not root: return count

      count = max(dfs(root.right, count), dfs(root.left, count))
      return count + 1

  return dfs(root, 0)


def maxDepth(root):
  if not root: return 0
  return 1 + max(maxDepth(root.left), maxDepth(root.right))


arr = [4,2,7,1,3,6,9]
print("original tree")
printTree(array_to_binary_tree(arr))
print("MAX DEPTH: ", maxDepth(array_to_binary_tree(arr)))

