#!/usr/bin/env python
# coding: utf-8

# ## 目標：應用插入排序法，將被選中的節點，與其前方所有的節點互相比較大小，並將小的放前方，直到所有節點都背比較並排序過為止
# #### Leetcode題目位置：https://leetcode.com/problems/insertion-sort-list/

# In[2]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        dummyHead = ListNode(0)  # DummyHead是虛擬節點，指向鍊表表頭head   # 一開始將表頭的值設為0
        dummyHead.next = ListNode(head.val)  # 這裡的.next指的是節點(值 + 位址)
        
        p = head # Pointer of original
        q = dummyHead  # dummyHead.next = head
        while p:
            
            if q == dummyHead or p.val >= q.val:   # 當頭節點的值比虛擬節點的值大時，數字的順序不用改變
                q.next = ListNode(p.val)           # 下任虛擬節點 = 前任Head的值   # 也就是讓虛擬節點指向下一個
                p = p.next                         # 下任Head = 前任Head的位址
                q = q.next                         # 下任虛擬節點是現任虛擬節點的下一任
            elif p.val < q.val:                    # 但若當頭節點的值小於虛擬節點的值時 (兩個元素需對調，且頭節點還是原本的頭節點， 只有虛擬節點需要不斷左移和頭節點比大小
                pre = dummyHead                    
                cur = dummyHead.next                
                while cur.val < p.val:              
                    pre = cur                      
                    cur = cur.next                  
                
                node = ListNode(p.val)              
                pre.next = node                     
                node.next = cur                     
                p = p.next                          
                
        return dummyHead.next


# #### Submissions_結果
# ![147#_Insertion Sort List_submissions_截圖](https://github.com/agying/leetcode-practices/blob/master/Leetcode/Submission%E7%B5%90%E6%9E%9C%E6%88%AA%E5%9C%96/%23147_Insertion%20Sort%20List.jpg?raw=true)
