from read_data import get_graph_table
# graph = get_graph_table()
# print (graph)
class DisDegree(object):
    def __init__(self, graph):
        self.graph = graph
        self.ver_degree = {}
        self.dis_degree = {}

    def count_ver_degree(self):
        for ver in self.graph:
            num_degree = len(self.graph[ver])
            self.ver_degree[ver] = num_degree

    def count_distribution(self):
        for ver, degree in self.ver_degree.items():
            if degree not in self.dis_degree:
                self.dis_degree[degree] = 1
            else:
                self.dis_degree[degree] += 1

    def get_distribution(self):
        self.dis_degree = sorted(self.dis_degree.items(), key = lambda x:x[0])
        # x = 0
        # for key, value in self.dis_degree:
        #     x += value
        # print (x)
        return self.dis_degree

    def get_ver_degree(self):
        return self.ver_degree

def test():
    graph = get_graph_table()
    disdegree = DisDegree(graph)
    disdegree.count_ver_degree()
    disdegree.count_distribution()
    # print (disdegree.get_ver_degree())
    print (disdegree.get_distribution())

# test()


