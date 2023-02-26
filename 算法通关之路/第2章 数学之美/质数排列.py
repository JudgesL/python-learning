# 给出从1到n的数的设计排列方案 让所有的质数都被放在质数索引上 返回可能的方案总数 返回答案mod 10^9 +7 即可
# 本题其实就是质数在质数的位置全排列 非质数在非质数的位置全排列，将其可能性相乘即可
from typing import List
class Solution:
    def numPrimeArrangements(self,n:int) -> int:
        def factorial(n) -> int:
            if (n <= 1):
                return 1
            # 这里使用了递归 但是其实也可以用迭代
            return n*factorial(n-1)
        # 由于0<n<=100 因此这里选择全列出所有的质数 但是也可以用算法去求
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

        primeCount = 0
        # 这里在计算一共有多少个质数
        while(primes[primeCount] <= n):
            primeCount += 1
        return factorial(primeCount)*factorial(n-primeCount)%(10**9+7)
