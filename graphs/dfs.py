from collections import defaultdict 

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def dfsWithInMemoryStackHelper(self, v, visited):
    visited[v] = True
    print(v, " ")

    for i in self.graph[v]:
      if(visited[i] == False):
        self.dfsWithInMemoryStackHelper(i,visited)
  
  def dfsRecursion(self, s):
    visited = [False] * (len(self.graph))
    self.dfsWithInMemoryStackHelper(s,visited)

  def dsfUsingStack(self, s):
    visited = [False] * (len(self.graph))
    stack = []
    stack.append(s)
    visited[s] = True
    while stack:
      s = stack.pop()
      print(s, " ")
      for i in self.graph[s]:
         if(visited[i] == False):
            stack.append(i)
            # print(stack)
            visited[i] = True






g = Graph()
## add edges to graph
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.addEdge(3, 0) 
g.addEdge(3, 1) 


print ("Following is Depth First Traversal"
                  " (starting from vertex 2)") 

g.dsfUsingStack(2) 
print("===================")
g.dfsRecursion(2) 