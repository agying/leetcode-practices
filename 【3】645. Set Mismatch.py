#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        
        # 全部總和
        nums_sum = sum(nums)
        
        # 不重複總和
        unique_sum = sum(list(set(nums)))
        
        # 正確情況下總和
        correct_sum = n*(n+1) / 2
        
        duplicated_num = nums_sum - unique_sum
        missing_num = correct_sum - unique_sum
        
        missing_num = int(missing_num)
        duplicated_num = int(duplicated_num)
        
        return [duplicated_num, missing_num]    


# In[14]:


nums = [1, 2, 3, 3, 5, 6]
a = Solution()
a.findErrorNums(nums)


# In[ ]:




