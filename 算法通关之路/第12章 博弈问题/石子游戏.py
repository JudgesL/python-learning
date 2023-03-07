# 取石子游戏，由于石子有偶数堆 比如 1 2 3 4，如果先手玩家取1 后手就只能在2 中取
# 如果先手取4 后手就可以在1 3 中取。这意味着先手玩家可以完全单方面控制取的是奇数还是偶数堆
# 因此只要知道奇数和偶数堆石子谁更多。 先手必胜

# 假设ALEX知道他所有操作会产生的结果 记作L1,L2 find_max(left,right) = max(piles[left]+L1, piles[right]+L2)
# 求L1 L2需要看Lee的后续操作 他也需要拿到最多的石子 L1 = min(A1,A2) L2=min(A3,A4) A1-A4代表Lee操作产生新石堆以后Alex决策的结果
# max(
#       piles[left]+min(self.find_max(left+2,right,piles,mem),
#                       self.find_max(left+1,right-1,piles,mem),),
#       piles[right]+min(self.find_max(left+1,right-1,piles,mem),
#                        self.find_max(left,right-2,piles,mem),),))
from typing import  List
class Solution:
    def stoneGame(self, piles:List[int])-> bool:
        sum = 0
        for i in piles:
            sum += i
        mem = []
        for i in range(len(piles)):
            mem.append([0]*len(piles))
        return 2*self.find_max(0,len(piles)-1,piles,mem)>sum

    def find_max(self,left:int,right:int,piles:List[int],mem:List[List[int]])->int:
        if left<0 or right<0 or left>right:
            return 0
        if mem[left][right] != 0:
            return mem[left][right]
        if left == right:
            mem[left][right] = piles[left]
            return piles[left]
        max_stone = max(
                        piles[left]+ min(self.find_max(left+2,right,piles,mem),
                                         self.find_max(left+1,right-1,piles,mem),
                                         ),
                        piles[right]+ min(self.find_max(left+1,right-1,piles,mem),
                                          self.find_max(left,right-2,piles,mem),
                                          ))
        mem[left][right] = max_stone
        return max_stone

