#!/usr/bin/env python
# coding: utf-8

# In[12]:


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
        
        dummyHead = ListNode(0)  # DummyHead是虛擬節點，指向鍊表表頭head
        dummyHead.next = ListNode(head.val)  # 這裡的.next指的是節點(值 + 位址)
        
        p = head # Pointer of original
        q = dummyHead  # dummyHead.next = head
        while p:
            
            if q == dummyHead or p.val >= q.val:   # 當頭節點的值比虛擬節點的值大時，數字的順序不用改變
                q.next = ListNode(p.val)           # 下任虛擬節點 = 前任Head的值
                p = p.next                         # 下任Head = 前任Head的位址
                q = q.next                         # 下任虛擬節點是現任虛擬節點的下一任
            elif p.val < q.val:                    # 但若當頭節點的值小於虛擬節點的值時 (兩個元素需對調，且頭節點還是原本的頭節點， 只有虛擬節點需要不斷左移和頭節點比大小
                pre = dummyHead                    # 
                cur = dummyHead.next               # 
                while cur.val < p.val:             # 
                    pre = cur                      #
                    cur = cur.next                 # 
                
                node = ListNode(p.val)             # 
                pre.next = node                    # 
                node.next = cur                    # 
                p = p.next                         # 
                
        return dummyHead.next


# In[ ]:




