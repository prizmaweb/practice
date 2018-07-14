class Graph:
    def __init__(self):
        self.vertices={}
        self.visited={}
        
    def add_vertex(self,vertex):
        if self.vertices.has_key(vertex):
		return
        self.vertices[vertex]=[]
        self.visited[vertex]=False

    def add_edge(self,edge):
        vertex=edge[0]
        self.vertices[vertex].append(edge[1])


        

