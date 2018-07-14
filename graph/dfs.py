from  graph import Graph

visited=set()
def dfs(g):
    for v in g.vertices.keys():
        if v not in visited :
            dfsearch(v,g)

def dfsearch(v,g):
    visited.add(v)
    for w  in g.vertices[v]:
        if w not in visited:
            dfsearch(w,g)
    print v
        
if __name__=='__main__':
    g=Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_edge((1,2))
    g.add_edge((2,3))
    g.add_edge((2,5))
    dfs(g)

