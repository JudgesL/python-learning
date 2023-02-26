# 给定一个由1（陆地）和0（水）组成的二维网络 计算岛屿的数量 岛屿是通过水平方向或垂直方向上相邻的陆地连接而成的
# 用深度优先遍历 一个方向走到头
from typing import List
class Solution:
    def numIslands(self,grid:[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        ans = 0

        # 已经路过的就标注0
        def dfs(r,c):
            grid[r][c] = '0'
            # 向上衍生
            if r-1 >=0 and grid[r-1][c] == '1':
                dfs(r-1, c)
            # 向下衍生
            if r+1 <m and grid[r+1][c] == '1':
                dfs(r+1, c)
            # 向左衍生
            if c-1 >=0 and grid[r][c-1] == '1':
                dfs(r, c-1)
            if c+1 >=0 and grid[r][c+1] == '1':
                dfs(r,c+1)
        # 每次都会把连通区域完全探索
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans

    # 通过辅助栈把递归修改成迭代
    def numIslands_diedai(self,grid:List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(row, col):
            grid[row][col] = '0'
            stack = [[row,col]]
            # 通过入栈的方法提供回溯点
            while stack:
                r,c = stack[-1]
                if r-1 >=0 and grid[r-1][c]=='1':
                    stack.append([r-1,c])
                    grid[r-1][c] = '0'
                    # 这个地方是和递归的不同之处 因为不能按照顺序完全执行完 必须每次选一个分支并入栈
                    continue
                if r+1 >=0 and grid[r+1][c]=='1':
                    stack.append([r+1,c])
                    grid[r+1][c] = '0'
                    # 这个地方是和递归的不同之处 因为不能按照顺序完全执行完 必须每次选一个分支并入栈
                    continue
                if c-1 >=0 and grid[r][c-1]=='1':
                    stack.append([r,c-1])
                    grid[r][c-1] = '0'
                    # 这个地方是和递归的不同之处 因为不能按照顺序完全执行完 必须每次选一个分支并入栈
                    continue
                if c+1 >=0 and grid[r][c+1]=='1':
                    stack.append([r,c+1])
                    grid[r][c+1] = '0'
                    # 这个地方是和递归的不同之处 因为不能按照顺序完全执行完 必须每次选一个分支并入栈
                    continue
                # 如果都不符合 就必须回退 让stack pop出一个 进而能够进入另外的情况
                stack.pop()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i,j)
        return ans
    # BFS迭代
    def numIslands_BFSdiedai(self, grid: List[List[str]]) -> int:
        from collections import deque

        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        ans = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] = '0'
                    queue.append((i,j))
                    while len(queue) > 0:
                        top = queue.popleft()
                        r = top[0]
                        c = top[1]
                        if r - 1 >= 0 and grid[r-1][c] == '1':
                            grid[r-1][c] = '0'
                            queue.append((r-1,c))
                        # 这里并不会每次只执行一个分支 而是可以都执行
                        if r+1 < m and grid[r+1][c] == '1':
                            grid[r+1][c] = '0'
                            queue.append((r+1,c))
                        if c-1>=0 and grid[r][c-1] == '1':
                            grid[r][c-1] = '0'
                            queue.append((r,c-1))
                        if c+1 <n and grid[r][c+1] == '1':
                            grid[r][c+1] = '0'
                            queue.append((r,c+1))
        return ans

