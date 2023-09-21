class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def findParent(n):
            res = n

            while res != parent[res]:
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += 1
            else:
                parent[p2] = p1
                rank[p1] += 1
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res
