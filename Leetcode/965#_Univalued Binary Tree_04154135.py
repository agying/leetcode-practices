#!/usr/bin/env python
# coding: utf-8

# # 目標：當二叉樹中的數字不完全相同時，返回false；若完全相同，則返回true

# 題目位址：https://leetcode.com/problems/univalued-binary-tree/

# In[1]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        if not root:
            return Falue
        
        value = [root]
        
        while value:
            cur = value[-1]
            del value[-1]
            
            if not cur:
                continue
            if cur.val == root.val:
                pass
            else:
                return False
            
            value.append(cur.left)
            value.append(cur.right)
        
        return True


# ![965#_Univalued Binary Tree](https://github.com/agying/leetcode-practices/blob/master/Leetcode/Submission%E7%B5%90%E6%9E%9C%E6%88%AA%E5%9C%96/965%23_Univalued%20Binary%20Tree.jpg?raw=true)

# ### 參考資料：
# 走訪對照數字的方法部分，參考了下列網址方法二的部分思維；再自力結合append()，完成走訪和其他部分的程式碼
# * https://www.jianshu.com/p/fcedb4635798
