#!/usr/bin/env python
# coding: utf-8

# # 法一：偷吃步
# ###直接應用python的既有函式，如append、pop等

# In[50]:


class MyLinkedList1(object):

    def __init__(self):
        self.linkedlist = list()

    def get(self, index):
        if index < 0 or index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]

    def addAtHead(self, val):
        self.linkedlist.insert(0, val)

    def addAtTail(self, val):
        self.linkedlist.append(val)

    def addAtIndex(self, index, val):
        if 0 <= index and index <= len(self.linkedlist):
            self.linkedlist.insert(index, val)

    def deleteAtIndex(self, index):
        if 0 <= index and index < len(self.linkedlist):
            self.linkedlist.pop(index)

            
# 因為我想 print出 list中所有元素，因此參考下方網址的程式碼，才得以將所有list中的元素直接在結果中呈現
# https://github.com/dokelung/Python-QA/blob/master/questions/dunder/自己寫的數據類型使用print無法輸出每個元素.md

    def __str__(self):
        return str(self.linkedlist)

    def __repr__(self):
        return str(self)


# In[60]:


listtest = MyLinkedList1()
param_1 = obj.get(5)
listtest.addAtHead(11)
listtest.addAtTail(99)
listtest.addAtIndex(1, 55)
listtest.addAtIndex(2, 77)


# In[61]:


listtest
# 結果是 [11, 55, 77, 99]


# In[63]:


listtest.deleteAtIndex(3)
listtest
# 結果是 [11, 55, 77]


# # 法二：按照題目規定的來
# ### 但是難度對我來說有點高，第一次寫class在不少地方卡住

# In[ ]:


class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList2(object):
    
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self  # or self.head == None:  這是參考別人程式碼後發現是我沒注意到的
            return -1
        else:

    def addAtHead(self, val: int) -> None:
        

    def addAtTail(self, val: int) -> None:
        

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
    
        
    

