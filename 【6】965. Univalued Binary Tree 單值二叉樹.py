#!/usr/bin/env python
# coding: utf-8

# # 目標：當二叉樹中的數字不完全相同時，返回false；若完全相同，則返回true

# ## (一) 完全二叉樹(Complete Binary Tree)
# * 完全二叉樹生成節點的方式是由上往下、由左往右生成。且每一個父節點生出子節點數量最多不大於兩個(一生二二生四的意思)。
# 
# * 完全二叉樹與滿二叉樹最大的差別為滿二叉樹的最後一層節點數量是滿的，而完全二叉樹則是除了最後一層外，其餘階層的節點樹都是滿的。

# ## (二) 堆(heap)

# > 堆(heap)的成立有兩個原則，分別是(1) 父節點 > 子節點的值、(2) 完全二叉樹

# <img src = "完全二叉樹.jpg" style = "width:/250px; height:/200px"/>

# 以上圖為例，當i = 3時，值為3。 同時，
# 該節點的父節點為：(i - 1) / 2
# 該節點的兩個子節點分別為：2i + 1 和 2i + 2

# ### 堆積化(Heapify)

# In[63]:


def swap(List, i, j):
    temp = List[i]
    List[i] = List[j]
    List[j] = temp


# In[64]:


def heap_sort(tree, n, i):  # n表示節點樹、i表示要堆積化的節點編號
    # 找i的子節點1
    c1 = 2 * i + 1
    # 找i的子節點2
    c2 = 2 * i + 2
    
    if i >= n:
        return tree
    # 找父節點(i)和兩個子節點 誰最大，並且把最大的值設為父節點，較小的則成為子節點
    # 當還有子節點時!!
    while c2 < n:
        if tree[c1] > tree[i]:
            max_value = tree[c1]
            swap(tree, c1, i)
        elif tree[c2] > tree[i]:
            max_value = tree[c2]
            swap(tree, c2, i)
        else:
            max_value = tree[i]
    return heapify(tree, n, max_value)


# In[ ]:


# 陷入迴圈，不知道哪裡錯
T = [1, 2, 5, 6, 4, 3, 7]
heap_sort(T, len(T), 2)
T


# In[ ]:





# ### 參考資料：
# * https://www.youtube.com/watch?v=j-DqQcNPGbE
