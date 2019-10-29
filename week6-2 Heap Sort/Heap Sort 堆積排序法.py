#!/usr/bin/env python
# coding: utf-8

# # 目標：建立堆積排序的函數，排序數列內元素的大小

# # 重要觀念

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

# # 開始實作

# ## 1. 堆積化(Heapify)

# In[3]:


def swap(List, i, j):
    temp = List[i]
    List[i] = List[j]
    List[j] = temp


# In[10]:


def heapify(tree, n, i):  # n表示節點數量、i表示要堆積化的第幾個節點編號
    # 找i的子節點1
    c1 = 2 * i + 1
    # 找i的子節點2
    c2 = 2 * i + 2
    
    if i > n:
        return tree
    
    # 找父節點(i)和兩個子節點 誰最大，並且把最大的值設為父節點，較小的則成為子節點
    # 當還有子節點時!! 堆積化!!
    if c1 < n & tree[c1] > tree[i]:
        swap(tree, c1, i)
        heapify(tree, n, i)
    elif c2 < n & tree[c2] > tree[i]:
        swap(tree, c2, i)
        heapify(tree, n, i)


# In[11]:


T = [4, 10, 3, 5, 1, 2]
heapify(T, len(T), 0)
T


# #### 發現返回的list不是這樣，看過參考影片的說明後，我需要找tree[i]、tree[c1]、tree[c2]這三個當中最大的

# In[5]:


def swap(List, i, j):
    temp = List[i]
    List[i] = List[j]
    List[j] = temp


# In[13]:


def heapify(tree, n, i):  # n表示節點數量、i表示要堆積化的第幾個節點編號
    # 找i的子節點1
    c1 = 2 * i + 1
    # 找i的子節點2
    c2 = 2 * i + 2
    
    if i >= n:
        return tree
    
    # 找父節點(i)和兩個子節點 三個誰最大，並且把最大的值設為父節點，較小的則成為子節點
    # 最大的當父節點
    # 當還有子節點時!! 堆積化!!
    
    max_value = i
    
    if c1 < n & tree[c1] > tree[max_value]:
        max_value = c1
        swap(tree, max_value, i)
        heapify(tree, n, max_value)
        
    elif c2 < n & tree[c2] > tree[max_value]:
        max_value = c2
        swap(tree, max_value, i)
        heapify(tree, n, max_value)
        
    elif tree[i] == tree[max_value]:
        return tree


# In[14]:


T = [4, 10, 3, 5, 1, 2]
heapify(T, len(T), 0)
T


# #### 為甚麼呢？為甚麼改了之後返回的結果連變都不變!!
# 除錯整天後，試過各種方法，結果結果結果發現問題是出在"&"!! <br>
# 因為偷懶我那時在程式碼輸入**<font color = red>"&"</font>**，但我卻忘了python中我需要打的是`and`...

# In[5]:


def swap(List, i, j):
    temp = List[i]
    List[i] = List[j]
    List[j] = temp


# In[46]:


def heapify(tree, n, i):  # n表示節點數量、i表示要堆積化的第幾個節點編號
    
    # 找i的子節點1
    c1 = 2 * i + 1
    # 找i的子節點2
    c2 = 2 * i + 2
    
    if i >= n:
        return tree
    
    # 找父節點(i)和兩個子節點 三個誰最大，並且把最大的值設為父節點，較小的則成為子節點
    # 最大的當父節點
    # 當還有子節點時!! 堆積化!!
    
    max_value = i
    
    if c1 < n and tree[c1] > tree[max_value]:
        max_value = c1
        swap(tree, max_value, i)
        heapify(tree, n, max_value)
        
    elif c2 < n and tree[c2] > tree[max_value]:
        max_value = c2
        swap(tree, max_value, i)
        heapify(tree, n, max_value)
        
    elif tree[i] == tree[max_value]:
        return tree


# In[47]:


T = [4, 10, 3, 5, 1, 2]
heapify(T, len(T), 0)
T


# #### 很無語的，問題解決

# 即使解決了這個問題，但目前二叉樹返回的數列順序仍是錯誤的，問題是出在上方的堆積化函數只能針對tree[0]進行堆積化。<br>
# 我要改良函式，讓函式可以自己**把最後一個子節點的"父節點"抓出來**，而**該"父節點"以前的每一個節點都會是某個節點的父節點**

# ## 2. 最大堆積(Max - Heap)
# 
# * 兩大規則：<br>
#     * 1 . 父節點的值大於子節點 <br>
#     * 2 . 樹根(root)一定是所有節點的最大值

# In[67]:


def max_heap(tree, n):

    # 找最後一個節點的父節點
    last = n - 1

    """
    if n % 2 == 0:
        # 如果n是奇數，tree不是完美二叉樹，其父節點的編號為
        parent = (last - 1) / 2
    else:
        # 其父節點的編號為
        parent = (last - 1) // 2
    """
    # 上面括弧內符號內的程式，可以縮寫成
    parent = (last - 1) // 2

    # 當i從parent到0時，以1漸減  # python 中 in range(1, 5) 會返回 1, 2, 3, 4不包含五。 # 所以第二個是-1，其實是包含0之意
    for i in range(parent, -1, -1):
        heapify(tree, n, i)


# In[75]:


T = [4, 10, 3, 5, 1, 2]
max_heap(T, len(T))
T


# ## 3. 堆積排序(Heap_Sort)

# * 當最大堆積完成後，開始要進入"堆積排序法"的完結，有幾個順序需要被完成：
#     * (1) 數列必須先被排為最大堆積
#     * (2) 交換第一和最後一個節點
#     * (3) 消除最後一個節點
#     * (4) 剩下的數列再排成一次最大堆積
#     * (5) 堆積化最後一個節點

# In[90]:


def heap_sort(tree, n):
    max_heap(tree, n)
    
    for i in range(n - 1, 0, -1):
        swap(tree, 0, i)
        max_heap(tree, i)
        heapify(tree, i, 0)   # i是指剩下的節點數


# In[91]:


T = [2, 5, 3, 1, 10, 4]
heap_sort(T, len(T))
T


# ## 類別化(class)
# 以上是用`def`的方式完成，接下來想試著將這些都類別化

# In[1]:


class Heap_Sort_class():
    
    def swap(self, List, i, j):
        temp = List[i]
        List[i] = List[j]
        List[j] = temp
        
    def heapify(self, tree, n, i):  # n表示節點數量、i表示要堆積化的第幾個節點編號
    
        # 找i的子節點1
        c1 = 2 * i + 1
        # 找i的子節點2
        c2 = 2 * i + 2

        if i >= n:
            return tree

        # 找父節點(i)和兩個子節點 三個誰最大，並且把最大的值設為父節點，較小的則成為子節點
        # 最大的當父節點
        # 當還有子節點時!! 堆積化!!

        max_value = i

        if c1 < n and tree[c1] > tree[max_value]:
            max_value = c1
            self.swap(tree, max_value, i)
            self.heapify(tree, n, max_value)

        elif c2 < n and tree[c2] > tree[max_value]:
            max_value = c2
            self.swap(tree, max_value, i)
            self.heapify(tree, n, max_value)

        elif tree[i] == tree[max_value]:
            return tree
        
    def max_heap(self, tree, n):

        # 找最後一個節點的父節點
        last = n - 1
        parent = (last - 1) // 2

        # 當i從parent到0時，以1漸減  # python 中 in range(1, 5) 會返回 1, 2, 3, 4不包含五。 # 所以第二個是-1，其實是包含0之意
        for i in range(parent, -1, -1):
            self.heapify(tree, n, i)
    
    def heap_sort(self, tree):
        
        n = len(tree)
        self.max_heap(tree, n)

        for i in range(n - 1, 0, -1):
            self.swap(tree, 0, i)
            self.max_heap(tree, i)
            self.heapify(tree, i, 0)   # i是指剩下的節點數


# In[2]:


T = [2, -5, 3, 1, 10, 4]
a = Heap_Sort_class()
b = a.heap_sort(T)
T


# ## 完成！

# ### 參考資料：
# * 堆排序(Heapsort)：https://www.youtube.com/watch?v=j-DqQcNPGbE
# * 排序之堆積排序法(Heap Sort)；http://marklin-blog.logdown.com/posts/1910116
