#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet():
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def add(self, key):
        from Crypto.Hash import MD5
        a = MD5.new()
        a.update(key.encode("utf-8"))
        x = a.hexdigest()
        x = int(a.hexdigest(), 16)
        remainder = x % self.capacity
        
        remainder = ListNode(remainder)
        x = ListNode(x)
        
        if not self.data[remainder.val]:
            self.data[remainder.val] = remainder
            self.data[remainder.val].next = x
        else:
            now = self.data[remainder.val]
            
            while now.val != x.val and now.next:
                now = now.next
            if now.val != x.val:
                now.next = x
            else:
                return
            
    def remove(self, key):
        from Crypto.Hash import MD5
        a = MD5.new()
        a.update(key.encode("utf-8"))
        x = a.hexdigest()
        x = int(a.hexdigest(), 16)
        remainder = x % self.capacity
        
        remainder = ListNode(remainder)
        x = ListNode(x)
        
        if self.data[remainder.val]:
            now = self.data[remainder.val]
            while now.val != x.val and now.next:
                former = now
                now = now.next
                
            former.next = now.next

        else:
            return
    
    
    def contains(self, key):
        from Crypto.Hash import MD5
        a = MD5.new()
        a.update(key.encode("utf-8"))
        x = a.hexdigest()
        x = int(a.hexdigest(), 16)
        remainder = x % self.capacity
        
        remainder = ListNode(remainder)
        x = ListNode(x)
        
        if self.data[remainder.val].val == remainder.val:
            now = self.data[remainder.val]
            
            while now.val != x.val and now.next:
                now = now.next
            if now.val == x.val:
                return True
            else:
                return False
                
        else:
            return False

