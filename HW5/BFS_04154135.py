#!/usr/bin/env python
# coding: utf-8

# In[4]:


from collections import defaultdict 
stat1 = []
stat2 = []

class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v)
        
        
    def BFS(self, s): 

        global stat1
        global stat2

        if s in self.graph:
            if s not in stat1:
                stat1.append(s)
            else:
                pass
        else:
            return []
        

        for i in range(len(self.graph[s])):
            if self.graph[s][i] in stat1 or self.graph[s][i] in stat2:
                pass
            else:
                stat1.append(self.graph[s][i])
            i = i + 1

        if s in stat2:
            pass
        else:
            stat2.append(s)
            del stat1[0]
        

        if stat1 != []:
            self.BFS(stat1[0])
            
        else:
            print(stat2)
            stat1 = []
            stat2 = []
            
            
    def DFS(self, s): 
        global stat1
        global stat2
        
        if s in self.graph:
            stat2.append(s)
        else:
            return []
        
        for i in range(len(self.graph[s])):
            if self.graph[s][i] in stat1 or self.graph[s][i] in stat2:
                pass
            else:
                stat1.append(self.graph[s][i])
            i = i + 1
        
        if stat1 != []:
            last = stat1[-1]
            del stat1[-1]
            self.DFS(last)
        else:
            print(stat2)
            stat1 = []
            stat2 = []

