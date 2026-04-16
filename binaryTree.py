from typing import Optional, List
from collections import deque

"""
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # leetcode 102
    # 二叉树

    # 空值
    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            # 当前头
            node = queue.popleft()

            # 更新level
            level.append(node.val)

            # 更新 子节点
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)

    return result

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    # leetcode 94
    # 中序遍历: 左根右 (stack)

    # 特殊情况
    if not root:
        return []
    
    ans = []        # result record
    stack = []      # 
    cur = root      

    while cur or stack:

        # 处理左子树
        while cur:
            stack.append(cur)
            cur = cur.left
        
        # 左子树结束
        # 退回根节点
        cur = stack.pop()
        ans.append(cur.val)
        
        # 转向右子树
        cur = cur.right 

    return ans

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    leetcode 144
    前序遍历: root -left -right
    """
    if not root:
        return []
    
    ans = []    # 记录最终回答  
    stack = [root]  # 记录node

    while stack:
        # stack - LIFO
        cur = stack.pop()
        ans.append(cur.val)
        
        """
        先压右后压左
        """
        if cur.right:
            stack.append(cur.right)
        
        if cur.left:
            stack.append(cur.left)

    return ans

def postorderTraversal( root: Optional[TreeNode]) -> List[int]:
    """
    leetcode 145
    后序遍历: 
    """
    if not root:
        return []
    
    ans= []
    stack = []
    cur = root
    prev = None  # 后序额外参数，用以控制 右子树是否结束

    # 要处理左 && 右子树 再 根node
    while cur or stack:
        # 左子树
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack[-1]     # 取最后一位

        # 右子树判断
        # 1. 右子树已遍历
        # 2. 右子树为空
        if cur.right == prev or not cur.right:
            cur = stack.pop()
            ans.append(cur.val)
            prev = cur
            cur = None
        # 右子树未
        # 计算
        else:
            cur = cur.right

    return ans
    
def maxPathSum(root: Optional[TreeNode]) -> int:
    # leetcode 124
    if not root:
        return 0
    
    ans = 0
    cur = root
    stack = []
    prev = None

    while cur or stack:
        temp = 0
        # 左子树
        while cur: 
            stack.append(cur.left)
            cur = cur.left
        
        cur = stack[-1]
        
        # 右子树判断
        if not cur.right or cur.right ==  prev:
            temp += cur
            



