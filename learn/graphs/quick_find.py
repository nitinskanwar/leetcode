class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, vertex):
        return self.root[vertex]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
print(uf.root)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
print(uf.root)
uf.union(2, 5)
print(uf.root)
uf.union(5, 6)
print(uf.root)
uf.union(6, 7)
print(uf.root)
uf.union(3, 8)
print(uf.root)
uf.union(8, 9)
print(uf.root)

print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false

# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.root)
print(uf.connected(4, 9))  # true