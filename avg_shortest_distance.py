import numpy as np
from read_data import get_graph_table
import time
class Distance(object):
    def __init__(self, graph):
        self.graph = graph
        self.diameter = 0
    
    def create_table(self):
        self.num_vertices = len(self.graph)
        self.dis_table = [([65535] * (self.num_vertices+1)) for i in range(self.num_vertices+1)]
        # print (self.dis_table)
        for i in range(1, self.num_vertices+1):
            self.dis_table[i][i] = 0
            # print (self.dis_table)
        # print (self.graph)
        # print (self.dis_table)
        for ver1, value in self.graph.items():
            for ver2 in value:
                self.dis_table[int(ver1)][int(ver2)] = 1
        # print (self.dis_table)
        self.dis_table = np.array(self.dis_table)

    def floyed(self):
        for k in range(1, self.num_vertices+1):
            print (k)
            for i in range(1, self.num_vertices+1):
                for j in range(1, self.num_vertices+1):
                    if self.dis_table[i][k] + self.dis_table[k][j] < self.dis_table[i][j]:
                        self.dis_table[i][j] = self.dis_table[i][k] + self.dis_table[k][j]

    def bfs(self):
        self.shortest_table = [([65535] * (self.num_vertices)) for i in range(self.num_vertices)]
        for i in range(0, self.num_vertices):
            self.shortest_table[i][i] = 0       
        for i in range(1, self.num_vertices+1):
            # 对每个节点分别进行遍历
            print (i)
            traversed = [str(i)] # 用来记录哪些节点已经遍历通过
            level = 1 # 用来定义遍历到第几层
            cur_to_traverse = self.graph[str(i)] # 用来记录当前阶段要遍历的邻接节点
            while len(cur_to_traverse) != 0:
                next_to_traverse = [] # 用来存储下一阶段要遍历的节点
                for item in cur_to_traverse:
                    if level > self.diameter:
                        self.diameter = level
                    # 对于每一个待遍历的邻居节点
                    self.shortest_table[i - 1][int(item) - 1] = level # 求当前节点到该节点的距离
                    # self.shortest_table[int(item) - 1][i - 1] = level
                    traversed.append(item)
                    for key in self.graph[item]:
                        if key not in traversed and key not in next_to_traverse and key not in cur_to_traverse:
                            next_to_traverse.append(key)
                level += 1
                cur_to_traverse = [item for item in next_to_traverse]
                # print (traversed, cur_to_traverse)

    def avg_dis(self):
        self.shortest_table = np.array(self.shortest_table)
        print (self.shortest_table.sum(), self.shortest_table.sum()/(self.num_vertices * (self.num_vertices-1)))

    def write2txt(self):
        np.savetxt("result.txt", numpy_data)

    def get_diameter(self):
        print (self.diameter)
        return self.diameter

graph = get_graph_table()
distance = Distance(graph)
distance.create_table()
time_start=time.time()
distance.bfs()
time_end=time.time()
print('totally cost',time_end-time_start)
distance.avg_dis()
distance.get_diameter()