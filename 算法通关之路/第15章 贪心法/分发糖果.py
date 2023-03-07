# n个孩子站成一条直线 预先评分 每个孩子至少一个 相邻的孩子中评分高的必须更多
# 由于糖果的数量同时受到左相邻和右相邻的影响 因此很难找到一个顺序去确定到底应该给几颗糖果
# 比如 1 2 2 那应该给 1 2 1颗糖果 但是如果是 1 2 2 1 那糖果数量就变成了 1 2 2 1 因此即使关注左右也很难确定到底几颗
# 这个时候我们把任务分解为 只关心左相邻 和 只关心右相邻 然后进行合并（取最大值）
# 这启发我们处理问题的时候可以将复杂的限制条件拆解成多个子限制 然后从局部最优推定全局最优
from typing import List
class Solution:
    def candy(self,ratings:List[int])->int:
        left_ans,right_ans = [1]*len(ratings),[1]*len(ratings)
        ans = 0
        # 先考虑左相邻
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                left_ans[i] = left_ans[i-1] + 1
        # 考虑右
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                right_ans[i] = right_ans[i+1] + 1

        for i in range(0,len(ratings)):
            ans += max(left_ans[i],right_ans[i])
        return ans
    