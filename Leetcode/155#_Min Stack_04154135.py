#!/usr/bin/env python
# coding: utf-8

# ## 目標：使一個Stack的資料陣列，具有放入(`push`)、跳出(`pop`)、求最後被放入stack的物品(`top`)，以及Stack中的最小值(`getMin`)的功能
# > Stack(堆疊)具有先進後出的特性，就像平常裝箱時，先裝入箱子的物品直到最後才會被取出
# #### Leetcode題目位址：https://leetcode.com/problems/min-stack/

# In[31]:


class MinStack:

    # 先對外宣告stack是一個list
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        if len(self.stack) < 0:
            return -1
        else:
            self.stack.append(x)

    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            self.stack.pop()

#   跳出盤子最上方的數值，也就是最後被放上list的值
    def top(self):
        if len(self.stack) <= 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        return min(self.stack)
    
# ---------下方兩行Leetcode不需要，但這兩行可以使我們在Jupyter Notebook中看到返回的數值為多少，而不是存放的位置---------
    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return str(self)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# In[32]:


stackobj = MinStack()
stackobj.push(51)
stackobj.push(4)
stackobj.push(5)
stackobj.push(9)
stackobj


# In[33]:


stackobj.pop()
stackobj


# In[34]:


# 在stack中如同盤子堆疊，先進後出，最上面的盤子是最晚被放上去的
stackobj.top()


# In[35]:


stackobj.getMin()


# #### Submissions_結果
# ![155_Min_Stack_submissions_截圖](https://github.com/agying/leetcode-practices/blob/master/Leetcode/Submission%E7%B5%90%E6%9E%9C%E6%88%AA%E5%9C%96/%23155_Min%20Stack.jpg?raw=true)
