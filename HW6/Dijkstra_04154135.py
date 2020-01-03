#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def Dijkstra(self, s):
        
        t = dict()
        t[0] = 0
        i = len(self.graph)
        s_list = []
        
        while i >= 0:
            # s_list是走訪的節點順序
            s_list.append(s)    # 先從起點開始
            
            for j in range(len(self.graph[s])):
               
                if self.graph[s][j] != 0:      
                    
                    if j not in t:
                        t[j] = t[s] + self.graph[s][j]
                    else:
                        if t[j] > t[s] + self.graph[s][j]:
                            t[j] = t[s] + self.graph[s][j]
                        else:
                            pass
            
            sh = {}
            for k1, v1 in t.items():     
                if k1 not in s_list:
                    sh[k1] = v1
                    shortest = min(sh.items(), key = lambda x: x[1])
            
            s = shortest[0]

            i = i - 1
            
        t = dict(sorted(t.items()))
        t = {str(k):v for k, v in t.items()}
        return t
    
    def Kruskal(self):
        return {}
        
    def addEdge(self, u, v, w): 
        
        self.graph.append([u, v, w])
        self.graph = sorted(self.graph, key = lambda l:l[2])
        
    def stat(self):
        
        parent_link = {}
        
        for i in range(len(self.graph)):
            parent_link[self.graph[i][0]] = -1
            parent_link[self.graph[i][1]] = -1

