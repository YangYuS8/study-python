# 题目描述
# 第一行表示输入的行数N，然后输入N行字符串，每行表示无向图的一个顶点和与该顶点相连的其他顶点及边的长度。
# 输出图的顶点数、边数、边的总长度。
# 图中A点所在行字符串为："{'A':{'B':2, 'D':7, 'O':2}}"。
# 提示：用eval函数处理输入字符串。
N = int(input().strip())
vertices = set()
edges_set = set()
total_weight = 0

for _ in range(N):
    line = input().strip()
    data = eval(line)
    for u, neighbors in data.items():
        vertices.add(u)
        for v, w in neighbors.items():
            vertices.add(v)
            edge = (min(u, v), max(u, v))
            if edge not in edges_set:
                edges_set.add(edge)
                total_weight += w

num_vertices = len(vertices)
num_edges = len(edges_set)
print(num_vertices, num_edges, total_weight)