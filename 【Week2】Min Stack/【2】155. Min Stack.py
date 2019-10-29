#!/usr/bin/env python
# coding: utf-8

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


# In[ ]:




