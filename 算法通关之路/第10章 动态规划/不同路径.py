class Solution:
    def uniquePath(self,m:int,n:int)->int:
        dp =[[1]*n for _ in range(m)]

        for col in range(1,m):
            for row in range(1,n):
                dp[col][row] = dp[col-1][row] + dp[col][row-1]
        return dp[m-1][n-1]
    # 对空间复杂度进行优化
    def uniquePath_optimize(self,m:int,n:int)->int:
        dp = [1]*n
        for _ in range(1,m):
            for j in range(1,n):
                # 在第一行的时候 dp是全1，所以这里要以第2行为起点
                # 第二行的时候dp[j-1]保存的是来自左边 dp[j]保存的其实是前一行 也就是来自上面 因此可以这么操作
                dp[j] += dp[j-1]
        return dp[n-1]

    # 记忆化递归
    visited = {}
    def uniquePaths_mem(self,m:int,n:int)->int:
        if (m,n) in self.visited:
            return self.visited[(m,n)]
        if m == 1 or n == 1:
            return 1
        cnt = self.uniquePaths_mem(m-1,n)+self.uniquePaths_mem(m,n-1)
        self.visited[m,n] = cnt
        return cnt