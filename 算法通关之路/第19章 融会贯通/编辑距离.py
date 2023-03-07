# 给定两个单词 word1 和 word2 计算出将 word1转换成word2所使用的的最少操作次数 可以插入删除或替换一个字符
class Solution:
    def helper(self,word1:str,s1:int,e1:int,word2:str,s2:int,e2:int,memo:dict)->int:
        # 比较已经结束 只需要删除或添加部分字符
        if s1 > e1:
            return e2 - s2 + 1
        elif s2 > e2:
            return e1 - s1 + 1
        # 比较的位置
        c1 = word1[s1]
        c2 = word2[s2]
        key = (s1,s2)
        if key in memo:
            return memo[key]
        if c1 == c2:
            memo[key] = self.helper(word1, s1+1,e1,word2,s2+1,e2,memo)
            return memo[key]
        else:
            memo[key] = min(
                            # delete or add s1
                            self.helper(word1,s1+1,e1,word2,s2,e2,memo),
                            # delete or add s2
                            self.helper(word1,s1,e1,word2,s2+1,e2,memo),
                            # shift
                            self.helper(word1,s1+1,e1,word2,s2+1,e2,memo)
                            ) + 1
        return memo[key]

    def minDistance(self,word1:str,word2:str)->int:
        return self.helper(word1,0,len(word1)-1,word2,0,len(word2)-1,dict())

    # 动态规划问题
    def minDistance_dongtai(self,word1:str,word2:str)->int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for j in range(n+1)]for i in range(m+1)]
        # 初始化
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        return dp[m][n]

    # 进一步优化的方法：dp[i][j]只用到i i-1 ,j j-1的数据，因此维护两行就够了。

