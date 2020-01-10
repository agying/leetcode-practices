#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution():
    
    def merge_sort(self, List):
    
    # 以下為曾在上方定義的cut_list
        if len(List) <= 1:
            return List

        half = len(List) // 2
        left = List[:half]
        right = List[half:]

        # 遞迴
        cut_left = self.merge_sort(left)
        cut_right = self.merge_sort(right)


        # 以下為曾在上方定義的compare_and_merge(cut_left, cut_right)

        combine_list = []

        i = j = 0
        while i < len(cut_left) and j < len(cut_right):

            # 比大小
            if cut_left[i] >= cut_right[j]:
                combine_list.append(cut_right[j])
                j = j + 1
            else:
                combine_list.append(cut_left[i])
                i = i + 1

            # 但當如果沒有可以比較的對象時，combine_list需要直接將"剩下的list" append加入
            if i == len(cut_left):
                combine_list = combine_list + cut_right[j:]
            elif j == len(cut_right):
                combine_list = combine_list + cut_left[i:]

        return combine_list

