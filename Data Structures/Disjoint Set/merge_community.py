# Enter your code here. Read input from STDIN. Print output to STDOUT

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
        
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        
        if ra == rb:
            return
        
        if self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
        elif self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
            self.size[rb] += self.size[ra]
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
            self.size[ra] += self.size[rb]


def merge_community(n, queries):
    uf = UnionFind(n)
    
    for query in queries:
        if len(query) == 3:
            uf.union(int(query[1]) - 1, int(query[2]) - 1)
        else:
            parent = uf.find(int(query[1]) - 1)
            print(uf.size[parent])


if __name__ == '__main__':
    n, q = list(map(int, input().rstrip().split()))
    
    queries = []
    
    for _ in range(q):
        query = input().rstrip().split()
        queries.append(query)
        
    merge_community(n, queries)
