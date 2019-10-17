#!/usr/bin/env python
# coding: utf-8

# ### 先不定義，先釐清步驟再寫函式
# #### 法一) 很想用卻不能用的方法

# In[4]:


a = [3, 7, 4, 5, 9, 1, 8, 2, 6]
a.sort()
a


# #### 法二) 試著應用Qucik Sort的方法，將數列分成幾部分，再令元素間互相比較

# In[151]:


a = [3, 7, 4, 5, 9, 1, 8, 2, 6]

# 找到數列排中間的數字
med = a[len(a) // 2]

# 讓 med 和 a 中的其他數字比大小，大的放右邊，小的放左邊
right = []
left = []

i = 0
while i in range (0, len(a) - 1):
    
    if med <= a[i]:
        right.append(a[i])
    else:
        left.append(a[i])
    
    i = i + 1


# In[152]:


# 讓左右各自找出各自的排中間數字
left_med = left[int(len(left) // 2)]

# 讓left_med 和 left 中的其他數字比大小，大的在右邊，小的在左邊
left_right = []
left_left = []

i = 0
while i in range(0, len(left) - 1):
    
    if left_med <= left[i]:
        left_right.append(left[i])
    else: 
        left_left.append(left[i])
        
    i = i + 1
    


# In[153]:


[left, med, right]


# 然後再一直切切切，切到每一個左右邊的新數列元素只有一個，此時數列a就是以大小順序排序了...

# 問題來了，我不能一直重複幫數列命名，我需要定義函式

# #### 法三) 遞迴函式讓程式幫我搞定一切

# In[225]:


def Split(List):

    right = []
    left = []
    med_list = []
    
    if len(List) <= 1: 
        return List

    med = List[(len(List) // 2)]

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


# In[226]:


b = [3, 7, 4, 5, 9, 1, 8, 2, 6]
Split(b)


# 想試試class法

# In[248]:


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


# In[249]:


b = [3, 7, 4, 5, 9, 1, 8, 2, 6]
a = Quick_Sort()
c = a.Split(b)


# In[250]:


c

