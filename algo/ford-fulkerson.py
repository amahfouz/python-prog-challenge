'''
Created on Aug 31, 2014

@author: amahfouz

Ford-Fulkerson implementation
'''

class Edge():
    def __init__(self, u, v, c):
        self.source = u
        self.sink = v
        self.capacity = c
        
    def __repr__(self):
        return "%s --- %s --->%s", self.source, self.sink, self.capacity

class Network():
    def __init__(self, num_verts):
        self.adj = [[] for _ in range(0, num_verts)]
        self.flow = {}
        
    def add_edge(self, u, v, c=0, rev_c=0):
        edge = Edge(u, v, c)
        redge = Edge(v, u, rev_c)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
        
    def find_path(self, source, sink, path):
        if (source == sink):
            return path
        
        for edge in self.adj[source]:
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path(edge.sink, sink, path + [edge])
                if (result != None):
                    return result
                
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            flow = min([edge.capacity - self.flow[edge] for edge in path])
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
            
        return sum([self.flow[edge] for edge in self.adj[source]])
    
## main test

n = Network(5)

n.add_edge(0, 2, 1)
n.add_edge(0, 3, 1)
n.add_edge(0, 4, 1)

n.add_edge(2, 1, 1)
n.add_edge(3, 1, 1)
n.add_edge(4, 1, 1)

n.add_edge(2, 3, 1000, 1000)
n.add_edge(2, 4, 1000, 1000)

print n.max_flow(0, 1)
    
            
                
                
                
        
        
        