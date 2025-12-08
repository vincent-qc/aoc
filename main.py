import bisect
import math

from util import file, next_int, next_line, next_line_ints, next_word, read_whole

N = 1000
M = 1000


class UF:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.size = {}

    def get_parent(self, x):
        if x not in self.parent:
            return -1
        else:
            return self.parent[x]

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.size[x] = 1

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def get_size(self, x):
        return self.size[self.find(x)]

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def weight(v1, v2):
    (a, b, c) = v1
    (x, y, z) = v2
    return math.sqrt((x-a)**2+(y-b)**2+(z-c)**2)


def solve():
    vertices = []
    edges = []

    for _ in range(N):
        [x, y, z] = list(map(int, next_line().split(',')))
        vertices.append((x, y, z))

    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            v1 = vertices[i]
            v2 = vertices[j]
            w = weight(v1, v2)
            edges.append((w, v1, v2))

    edges.sort()
    print(edges[0])
    uf = UF(len(vertices))

    added = 0
    idx = 0
    while added < len(vertices)-2:
        edge = edges[idx]
        (_, v1, v2) = edge
        if uf.union(v1, v2):
            added += 1
        idx += 1

    while idx < len(edges):
        edge = edges[idx]
        (_, v1, v2) = edge
        idx += 1
        print(idx)
        if uf.union(v1, v2):
            (x1, _, _) = v1
            (x2, _, _) = v2
            print("ANS ", x1*x2)
            return

        # sizes = []
        # seen = set()

        # for v in vertices:
        #     p = uf.find(v)
        #     if p in seen:
        #         continue
        #     seen.add(p)
        #     print(p)
        #     sizes.append(uf.get_size(p))

        # sizes.sort(reverse=True)
        # three = sizes[:3]

        # print(sizes)

        # product = three[0] * three[1] * three[2]
        # print(product)


pass

solve()
