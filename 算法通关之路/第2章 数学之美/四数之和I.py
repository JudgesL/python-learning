# 给定4个整数列表ABCD 判断nums中是否存在4个元素a,b,c,d 使a+b+c = target，找出所有满足条件且不重复的四元组
from typing import List
class Solution:
    def fourSumCount(self, A:List[int], B:List[int],C:List[int],D:List[int]) -> int:
        mapper = {}
        res = 0
        for i in A:
            for j in B:
                # 这里把A中的项i 和B中的项j 的和作为key保存到哈希表中，如果存在有一样的，那就取出这个值并+1，如果没有就返回0+1
                mapper[i+j] = mapper.get(i+j,0) + 1
        for i in C:
            for j in D:
                # 如果能从哈希表中取出一个 -(i+j)的项，代表加起来会是0，因此就可以加到res中
                res += mapper.get(-1*(i+j),0)
        return res

solve = Solution()
A=[1, 2]
B=[-2,-1]
C=[-1,2]
D=[0,2]
answer = solve.fourSumCount(A,B,C,D)
print(answer)