class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.isConnected = isConnected
        self.n = len(isConnected)
        self.province = 0
        self.visited = [False] * self.n
        for i in range(self.n):
            if self.visited[i] != True:
                self.province += 1
                self.dfs(i)
        
        return self.province



    def dfs(self, node):
        self.visited[node] = True
        for i in range(self.n):
            if self.isConnected[node][i] == 1 and self.visited[i] != True:
                self.dfs(i)
