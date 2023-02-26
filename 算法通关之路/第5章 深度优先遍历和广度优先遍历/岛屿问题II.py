# 给定m行 n列的二维网络 网络最开始全部被水充满 通过addLand增加陆地 输出每次操作后的岛屿数量
# 因为地图并非一开始就给定 用DFS和BFS效率都很低 因此采用查并集的方法
class Solution:
    class UnionFind:
        def __init__(self,grid):
            self.count = 0
            m = len(grid)
            n = len(grid[0])
            self.parent = [0 for _ in range(m*n)]
            self.rank = [0 for _ in range(m*n)]
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '1':
                        self.parent[i*n+j] = i*n+j
                        self.count += 1
        def find(self,i):
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

        def union(self,x,y):
            rootx = self.find(x)
            rooty = self.find(y)
            if rootx!= rooty:
                if self.rank[rootx] > self.rank[rooty]:
                    self.parent[rooty] = rootx
                elif self.rank[rootx] < self.rank[rooty]:
                    self.parent[rootx] = rooty
                # 最初的rank都是0 当出现了第一次合并以后 y归属到x之下 并且x的优先级+1 以后以优先级最高的为基础进行合并
                else:
                    self.parent[rooty] = rootx
                    self.rank[rootx] += 1
                self.count -= 1

        def getCount(self):
            return self.count

        def setCount(self, count):
            self.count = count

        def setParent(self,i, val):
            self.parent[i] = val

    def numIslands(self,m,n,positions):
        if m <=0 or n<=0:
            return []
        ans = []
        grid = [[0 for _ in range(n)] for _ in range(m)]

        uf = self.UnionFind(grid)

        for i in range(len(positions)):
            position = positions[i]
            uf.setCount(uf.getCount()+1)
            uf.setParent(position[0]*n + position[1],position[0]*n +position[1])
            grid[position[0]][position[1]] = '1'
            if position[0] - 1 >= 0 and grid[position[0]-1][position[1]] == '1':
                uf.union(position[0]*n + position[1],(position[0]-1)*n + position[1])

            if position[0] + 1 < m and grid[position[0]+1][position[1]] == '1':
                uf.union(position[0]*n + position[1],(position[0]+1)*n + position[1])

            if position[1] - 1 >= 0 and grid[position[0]][position[1]-1] == '1':
                uf.union(position[0] * n + position[1], position[0] * n + position[1] - 1)

            if position[1] + 1 < n and grid[position[0]][position[1]+1] == '1':
                uf.union(position[0] * n + position[1], position[0] * n + position[1] + 1)

            ans.append(uf.getCount())

        return ans



