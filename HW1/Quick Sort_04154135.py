#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Quick_Sort():
    
    def find_med(self, List):
        # 定義找排行中間的數字函數
        return List[(len(List) // 2)]
    
    # 定義 把比 med 大的元素放到右邊數列，比 med 小的元素放到左邊數列
    def Split(self, List):

        if len(List) <= 1: 
            return List
        
        med = self.find_med(List)
    
        right = []
        left = []
        med_list = []
        
        i = 0
        for i in range (0, len(List)):

            if med < List[i]:
                right.append(List[i])
            elif med == List[i]:
                med_list.append(List[i])
            else:
                left.append(List[i])

            i = i + 1
            
        return Split(left) + med_list + Split(right)

