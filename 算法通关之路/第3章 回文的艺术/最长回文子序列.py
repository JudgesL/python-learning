# 给定一个字符串s 找到其中最长的回文子序列 可以假设s的最大长度为1000
# 假设字符串中间部分的最长回文子序列长度已经求出来了 就可以直接比较两边
# 如果两边相同 那+2 如果不同那不变
# 用一个dp[i][j]保存s[i:j+1]的最大回文子序列长度
class Solution:
    def longestPalidromeSubseq(self,s:str)->int:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        # i代表着左边
        # 因为dp[i][...]依赖于dp[i+1][...]因此外循环从后往前
        for i in reversed(range(n)):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
    # 因为dp[i][j]只需要dp[i+1][j]和dp[i][j-1]因此其实可以滚动刷新数组存储
    # 这里每次结束一轮i以后 就会把cur同步到pre里
    # 因此如果需要dp[i+1][...]实质上就是在找pre[...]
    def longestPalidromeSubseq_gundong(self,s:str)->int:
        n = len(s)
        pre = [0]*n
        cur = [0]*n
        for i in reversed(range(n)):
            for j in range(i,n):
                if i == j:
                    cur[j] = 1
                elif s[i] == s[j]:
                    cur[j] = pre[j-1] + 2
                else:
                    cur[j] = max(pre[j],cur[j-1])
            pre = cur.copy()
        return pre[-1]