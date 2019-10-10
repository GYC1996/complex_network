from read_data import get_graph_table
from dis_degree import DisDegree
class NodeBetweenness(object):
    def __init__(self, graph, id):
        self.graph = graph
        self.id = id
        self.betweenness = 0.0
    
    def get_betweenness(self):
        return self.betweenness

    def bfs(self, v1, v2):
        cur2traverse = self.graph[v1] # 当前待遍历的顶点
        traversed = [v1]
        path = 1
        while v2 not in cur2traverse:
            next2traverse = []
            for item in cur2traverse:
                traversed.append(item)
                path += 1
                # 遍历每一个当前阶段待遍历的节点
                vers = cur2traverse[item] # 待遍历节点所连接的下一个节点
                next2traverse = [item for item in vers if item not in traversed and item not in cur2traverse and item not in next2traverse]
            if next

    def count_betweenness(self):
        vers = [key for key in self.graph.keys()]
        for i in range(len(vers)):
            for j in range(i+1, len(vers)):
                if i != self.id and j != self.id:
                    self.bfs(vers[i], vers[j])
                    pass

graph = get_graph_table()
disdegree = DisDegree(graph)
disdegree.count_ver_degree()
ver_degree = disdegree.get_ver_degree()
key = max(ver_degree,key=ver_degree.get)
# 获取度最大的那个节点
# print (key, ver_degree[key])
nodebetween = NodeBetweenness(graph, key)