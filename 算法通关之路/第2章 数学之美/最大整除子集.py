# 给出一个无重复的正整数组成的集合 找出其中最大的整除子集
# 如果存在一个整数子集S 以及整数x x能够被S中最大的数整除，那么加入x就可以让S成为更大的整除子集
from typing import List
class Solution:
    def largestDivisibleSubset(self,nums:List[int]) -> List[int]:
        # base case for simplicity
        S = {-1:set()}
        nums.sort()
        # 每个x 都要进行一轮判断
        for x in nums:
            # 用于保存对每个x有可能存在的序列
            temp = []
            for d in S:
                # 如果x能整除保存的list的key 也就是list中的最大数，那就可以加入这个list
                if (x%d == 0):
                    S[d].add(x)
                    temp.append(S[d])
                    # 需要暂时移除 因为还需要考察是不是别的也可以加入进来
                    S[d].remove(x)
            # 在S中保存对于当前位置的最长可能性，并且用X的大小作为其索引。temp中保存的都是可以融入x的情况，因此在最后求个并集就可以
            S[x] = max(temp,key=len) | {x}
            print('S:',S)
        return list(max(S.values(),key=len))

solve = Solution()
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

answer = solve.largestDivisibleSubset(nums)
print(answer)
