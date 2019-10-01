#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        # 全部總和
        nums_sum = sum(nums)
        
        min_nums = min(nums)
        max_nums = max(nums)
        correct_sum = (min_nums + max_nums) * n / 2
        
        duplicated_num = correct_sun - nums_sum
        missing_num = duplicated_num + 1
        
        return [duplicated_num, missing_num]
    
#     def __str__(self):
#         return str(self.nums)

#     def __repr__(self):
#         return str(self)


# In[19]:


nums = [1, 2, 3, 4, 4, 5]
nums = Solution()
nums.findErrorNums


# In[ ]:




