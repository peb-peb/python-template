class UnionFind:
    def __init__(self, size) -> None:
        self.parents = [i for i in range(size)]
        self.size = [0 for _ in range(size)]
        self.groups = size
        
    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node

    def union(self, u, v):
        ultimate_parent_u = self.find(u)
        ultimate_parent_v = self.find(v)
        if ultimate_parent_u == ultimate_parent_v:
            return False
        if self.size[ultimate_parent_u] > self.size[ultimate_parent_v]:
            self.parents[ultimate_parent_v] = ultimate_parent_u
            self.size[ultimate_parent_u] += self.size[ultimate_parent_v]
        else:
            self.parents[ultimate_parent_u] = ultimate_parent_v
            self.size[ultimate_parent_v] += self.size[ultimate_parent_u]
        self.groups -= 1
        return True
