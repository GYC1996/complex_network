from read_data import get_graph_table
class ClusterCoefficient(object):
    def __init__(self, graph):
        self.graph = graph
        self.culster = {}

    def count_c(self):
        for key, value in self.graph.items():
            t = len(value) * (len(value) - 1) / 2
            if t == 0:
                e = 0
                c = 0
                self.culster[key] = c
            else:
                e = 0
                for i in range(len(value)):
                    for j in range(i+1, len(value)):
                        v1 = value[i]
                        v2 = value[j]
                        if v2 in self.graph[v1]:
                            e += 1
                c = float(e) / t
                self.culster[key] = c

    def avg_c(self):
        # print (self.culster)
        sum_value = 0
        for key, value in self.culster.items():
            sum_value += value
        return (sum_value / len(self.graph))

graph = get_graph_table()
clustercoefficient = ClusterCoefficient(graph)
clustercoefficient.count_c()
print (clustercoefficient.avg_c())

            

