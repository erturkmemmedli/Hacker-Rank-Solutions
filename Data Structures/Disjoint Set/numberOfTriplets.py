# Kundu and Tree


# Enter your code here. Read input from STDIN. Print output to STDOUT

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
    
    def union(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        
        if _a == _b:
            return
        
        if self.rank[_a] > self.rank[_b]:
            self.parent[_b] = _a
        elif self.rank[_a] < self.rank[_b]:
            self.parent[_a] = _b
        else:
            self.parent[_b] = _a
            self.rank[_a] += 1


def numberOfTriplets(n, edges):
    MOD = 10 ** 9 + 7
    uf = UnionFind(n)
    parents = {}
    triplets = combOf3(n)
    
    for a, b, color in edges:
        if color == 'b':
            uf.union(a - 1, b - 1)
        
    for i in range(n):
        p = uf.find(i)
        parents[p] = parents.get(p, 0) + 1
    
    for v in parents.values():
        triplets -= combOf3(v)
        triplets -= combOf2(v) * (n - v)
        
    return triplets % MOD
         
            
def combOf3(n):
    return 0 if n < 3 else n * (n - 1) * (n - 2) // 6
    
    
def combOf2(n):
    return 0 if n < 2 else n * (n - 1) // 2


if __name__ == '__main__':
    n = int(input())
    
    edges = []
    
    for _ in range(n - 1):
        query = input().rstrip().split()
        edges.append([int(query[0]), int(query[1]), query[2]])
    
    print(numberOfTriplets(n, edges))
