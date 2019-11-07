#!/usr/bin/env python
# coding: utf-8

# # 合併排序法
# 合併排序法是一個排序演算法，時間效率為O(nlogn)，和Quick Sort一樣是非常有效率的排序演算法。
# 其演算的邏輯為下：
# * 1. 切割串列，直到每個串列的組成只剩一個元素 
# * 2. 將相鄰的兩個元素互比大小，並做排序(如小的在左邊，大的在右邊)；此時每個串列皆由1~2個元素構成
# * 3. 將相鄰的兩個串列首項互比大小，並將較小的元素移到到另一個新list(append新的、刪除舊的)
# * 4. 將左右兩個最新的首項互比大小，同樣將較小的元素移到上述的新list中
# * 5. 重複3的操作直到兩個串列中的每個元素皆比過大小，按順序排序

# ## 1. 切割串列

# In[1]:


# 切割串列
def cut_list(List):
    if len(List) <= 1:
        return List
    
    half = len(List) // 2
    left = List[:half]
    right = List[half:]
    
    # 遞迴
    cut_left = cut_list(left)
    cut_right = cut_list(right)
    
    return cut_left, cut_right


# In[2]:


t = [2, 6, 4, 3, 8, 7, 1, 9, 5]
cut_list(t)


# 發現切割之後太多個()，想了很久發現是return那行表示法造成的，如果沒有return那行，`cut_list`的功能沒有錯誤，因此下方直接跳過return

# In[ ]:


# 切割串列
def cut_list(List):
    if len(List) <= 1:
        return List
    
    half = len(List) // 2
    left = List[:half]
    right = List[half:]
    
    # 遞迴
    cut_left = cut_list(left)
    cut_right = cut_list(right)


# ## 2. 比大小

# 上方`cut_list`使程式將list切割為以元素為單位的list，接下來需要進行：
# * (1) 兩兩list相比大小 (此時的list皆只有一個元素)
# * (2) 將list從小到大排序並合併<br>
# * (3) **使用遞迴，將上方(1)(2)重新比較並合併**

# In[37]:


def compare_and_merge(cut_left, cut_right):
    
    combine_list = []

    for i in range(0, len(cut_left)):
        for j in range(0, len(cut_right)):
               
            # 比大小
            if cut_left[i] >= cut_right[j]:
                combine_list.append(cut_right[j])
                j = j + 1
            else:
                combine_list.append(cut_left[i])
                i = i + 1
                
            # 但當如果沒有可以比較的對象時，combine_list需要直接將"剩下的list" append加入
            if i == len(cut_left):
                combine_list.append(cut_right[j:])
            elif j == len(cut_right):
                combine_list.append(cut_left[i:])
                  
    return combine_list    
    
a = [3,8,11,12]
b = [5, 9, 3]
compare_and_merge(a, b)


# #### 又鬼打牆
# for_loop不會搭配i = i + 1 !!!! <br>
# while才能控制i = i + 1 !!!

# In[45]:


def compare_and_merge(cut_left, cut_right):
    
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
    
a = [3]
b = [5]
compare_and_merge(a, b)


# ### 3. 合併`cut_list`和`compare_and_merge`兩個def

# In[50]:


def merge_sort(List):
    
    # 以下為曾在上方定義的cut_list
    if len(List) <= 1:
        return List
    
    half = len(List) // 2
    left = List[:half]
    right = List[half:]
    
    # 遞迴
    cut_left = merge_sort(left)
    cut_right = merge_sort(right)

    
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


# In[53]:


t = [2, 6, 3, 4, 8, 0, 7, 1, 9, 5]
merge_sort(t)


# ## 4. 製作成class的模式：

# In[116]:


class Solution():
    
    def merge_sort(self, List):

        # 以下為曾在上方定義的cut_list
        if len(List) <= 1:
            return List

        half = len(List) // 2
        left = List[:half]
        right = List[half:]

        # 遞迴
        cut_left = merge_sort(left)
        cut_right = merge_sort(right)


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


# In[117]:


t = [2, 6, 3, 4, 8, 0, 7, 1, 9, 5]
a = Solution()
a.merge_sort(t)


# ## 大功告成！

# ## 參考資料：
# * https://github.com/amirziai/learning/blob/master/algorithms/Merge-Sort.ipynb
