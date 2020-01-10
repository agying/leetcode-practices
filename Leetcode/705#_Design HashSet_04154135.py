#!/usr/bin/env python
# coding: utf-8

# ## 目標：使用哈希表(和Linked List)將資料按餘數存放，並可以刪除和搜尋樹值是否存在表中
# #### Leetcode題目位置：https://leetcode.com/problems/design-hashset

# In[7]:


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet(object):

    def __init__(self):
        self.capacity = 10000
        self.data = [None] * self.capacity
        
    def add(self, key):
        remainder = key % self.capacity
        now = self.data[remainder]
        if not now: 
            self.data[remainder] = ListNode(key)
            return
        if now.val == key:
            return 
        while now:
            if now.val == key: 
                return
            if not now.next: 
                now.next = ListNode(key)
                return 
            if now.next: 
                now = now.next
        return 

    def remove(self, key):
        remainder = key % self.capacity
        now = self.data[remainder]
        if not now:
            return 
        
        if now.val == key:
            self.data[remainder] = now.next
            
        while now.next:
            if now.next.val == key:
                now.next = now.next.next
                return 
            
            now = now.next
        return
        

    def contains(self, key):
        remainder = key % self.capacity
        now = self.data[remainder]
        while now:
            if now.val == key:
                return True
            now = now.next
        return False


# In[9]:


a = MyHashSet()
a.add(1)
a.add(2)
a.remove(1)
p = a.contains(1)
u = a.contains(2)
q = a.contains(3)

print(p)
print(u)
print(q)


# #### Submissions_結果
# ![705#_Design HashSet_截圖](https://github.com/agying/leetcode-practices/blob/master/Leetcode/Submission%E7%B5%90%E6%9E%9C%E6%88%AA%E5%9C%96/705%23Desigh%20HashSet.jpg?raw=true)
