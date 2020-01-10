#!/usr/bin/env python
# coding: utf-8

# ## 目標：在一list中的連續整數，有一個數字重複、且因此該數字的下一個數字沒有成功加入list中。此題需要找出重複之數, 未出現之數，並以陣列方式返回出來
# #### Leetcode題目位置：https://leetcode.com/problems/set-mismatch/

# In[1]:


class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        
        # 全部總和
        nums_sum = sum(nums)
        
        # 不重複總和
        unique_sum = sum(list(set(nums)))
        
        # 正確情況下總和
        correct_sum = n * (n + 1) / 2
        
        duplicated_num = nums_sum - unique_sum
        missing_num = correct_sum - unique_sum
        
        missing_num = int(missing_num)
        duplicated_num = int(duplicated_num)
        
        return [duplicated_num, missing_num]    


# In[2]:


nums = [1, 2, 3, 3, 5, 6]
a = Solution()
a.findErrorNums(nums)


# #### Submissions_結果
# ![645#_Set Mismatch_submissions_截圖](https://github.com/agying/leetcode-practices/blob/master/Leetcode/Submission%E7%B5%90%E6%9E%9C%E6%88%AA%E5%9C%96/645%23_Set%20Mismatch.jpg?raw=true)
