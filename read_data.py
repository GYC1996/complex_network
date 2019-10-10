# import 

class Graph(object):
    
    def __init__(self):
        self.num_vertices = 0
        self.num_edge = 0
        self.graph_table = {}

    def add_vertex(self, id):
        self.num_vertices += 1
        self.graph_table[id] = []
    
    def add_edge(self, v1, v2):
        self.num_edge += 1
        self.graph_table[v1].append(v2)
        self.graph_table[v2].append(v1)

    def get_vertex_num(self):
        # print (self.num_vertices)
        return self.num_vertices

    def get_edge_num(self):
        # print (self.num_edge)
        return self.num_edge

    def get_graph(self):
        return self.graph_table

g = Graph()
with open("edges.txt", "r") as fread:
    edges = fread.readlines()
    for edge in edges:
        v1v2 = edge.strip('\n').split(' ')
        v1 = v1v2[0]
        v2 = v1v2[1]
        if v1 not in g.graph_table:
            g.add_vertex(v1)
        if v2 not in g.graph_table:
            g.add_vertex(v2)
        g.add_edge(v1, v2)
# print (g.get_vertex_num(), g.get_edge_num())
# for key in g.graph_table:
#     print (key, g.graph_table[key])

def get_graph_table():
    print ("the number of vertices is", g.get_vertex_num())
    return g.get_graph()