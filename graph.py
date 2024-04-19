# 先定义一个邻接表
from collections import defaultdict
class Graph():
    def __init__(self) -> None:
        self.adj_list = defaultdict(list) # 初始化，字典里的每一个元素都是一个列表，
                                          # 顶点A对应的元素为 （顶点B，AB边的权重）
        
    def add_edge(self, a, b, weight = 1):
        self.adj_list[a].append((b, weight))
        self.adj_list[b].append((a, weight)) # 同时添加，保证对称
        

g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 4)

print(g1.adj_list)

# 深度优先遍历

def dfs(graph, start, visited=None):
    if not visited: # 初始化时设置为空集合
        visited = set()
    if start not in visited:
        visited.add(start) # 向集合中添加
        print(start)
        for node, _ in graph.adj_list[start]: # 遍历当前节点的所有邻接点，开始递归
            dfs(graph, node, visited)

# dfs(g1, 0)

# 广度优先遍历
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    while queue:
        cur = queue.popleft()
        visited.add(cur)
        print(cur)
        for node, _ in graph.adj_list[cur]:
            if node not in visited:
                queue.append(node)

bfs(g1, 0)