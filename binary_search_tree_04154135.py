#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():

    def insert(self, root, val):

        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                root.left = self.insert(root.left, val)
            else:
                root.right = self.insert(root.right, val)
            return root
        
    def search(self, root, target):
        
        # 深度優先 # 前序(Pre-Order)(VLR)
        
        if root is None:
            return None
        else:
            if target == root.val:
                return root
            elif target < root.val:
                return self.search(root.left, target)
            else:
                return self.search(root.right, target)
            
    def find_max(self, root):
    
        now = root
        while now.right:
            now = now.right
        return now
    
    def delete(self, root, target):
               
        if root is None:
            return root
        else:
            if target < root.val:
                root.left = self.delete(root.left, target)
                
            elif target > root.val:
                root.right = self.delete(root.right, target)
                
            else:
                # 當沒有子節點時
                if root.left is None and root.right is None:
                    root = None

                elif root.right is None or root.left is None:
                    if root.left:
                        root = root.left

                    else:
                        root = root.right
                        
                elif root.left and root.right:
                    # 左子樹的最大值取代被delete的節點
                    root.val = self.find_max(root.left).val
                    # 刪除取代人的那個節點(需要用遞迴自己)  # 也就是從左子樹中找到該值 # 然後刪掉(因為她沒有子節點，所以遞迴直接刪掉即可
                    root.left = self.delete(root.left, root.val)
        
        while self.search(root, target) is not None:
            root =  self.delete(root, target)
        
        return root

    def delete_element(self, root, target):
               
        if root is None:
            return root
        else:
            if target < root.val:
                root.left = self.delete_element(root.left, target)
                
            elif target > root.val:
                root.right = self.delete_element(root.right, target)
                
            else:
                # 當沒有子節點時
                if root.left is None and root.right is None:
                    root = None

                elif root.right is None or root.left is None:
                    if root.left:
                        root = root.left

                    else:
                        root = root.right
                        
                elif root.left and root.right:
                    # 左子樹的最大值取代被delete的節點
                    root.val = self.find_max(root.left).val
                    # 刪除取代人的那個節點(需要用遞迴自己)  # 也就是從左子樹中找到該值 # 然後刪掉(因為她沒有子節點，所以遞迴直接刪掉即可
                    root.left = self.delete_element(root.left, root.val)
            return root
    
    
    def modify(self, root, target, new_val):
        
        
        if root is None:
            return root
        
        while self.search(root, target) is not None:
            root = self.delete_element(root, target)
            root = self.insert(root, new_val)
            root = self.modify(root, target, new_val)
        return root
        
    # print出樹的長相，方便檢查是否有錯
    def preorder(self, root):
        if root is not None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

