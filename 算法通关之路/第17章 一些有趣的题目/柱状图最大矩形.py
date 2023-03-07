# 核心思想 用f(i）表示以i作为最低点能够成的矩形的最大面积
# 在向左寻求第一个高于的值的时候 如果在判断的这个柱子（j）小于我们的比较柱（i），我们可以直接调到第一个比j柱子更大的位置 中间部分显然是满足的
from typing import List
class Solution:
    def largestRectangleArea(self,heights:List[int])->int:
        n = len(heights)
        l,r,ans = [-1]*n,[n]*n,0
        for i in range(1,n):
            j = i-1
            # 找第一个最小的
            while j>=0 and heights[j]>=heights[i]:
                j = l[j]
            l[i] = j

        for i in range(n-2,-1,-1):
            j = i+1
            while j<n and heights[j]>=heights[i]:
                j = r[j]
            r[i] = j

        for i in range(n):
            ans = max(ans,heights[i]*(r[i]-l[i]-1))
        return ans
    # 单调栈
    def largestRectangleArea_dandiao(self,heights:List[int])->int:
        #左右哨兵0
        n,heights,st,ans = len(heights),[0]+heights+[0],[],0
        for i in range(n+2):
            print('i=',i)
            print('st:',st)
            # 如果遇到了更高的元素 就直接压到栈里了 如果遇到的是更低的 那代表找到了柱子
            # 每个数字一旦出单调栈 就意味着其解已经找到
            # 这个位置的右端点就是遇到的这个 它更小 另外一个端点就是栈顶 因为这个数更大它才被压入 所以栈顶一定更小
            # 这个步骤不会有例外 因为这个新数字会把之前比他大的全都出栈自己才能入栈，所以等到它自己出的时候也满足左右
            while st and heights[st[-1]] > heights[i]:
                print('while_st:', st)
                print('heights[st[-1]]',heights[st[-1]])
                print('heights[i]',heights[i])
                ans = max(ans,heights[st.pop(-1)]*(i-st[-1]-1))
                print('ans=', ans)
            st.append(i)
            print('append_st:', st)

        return ans

solve = Solution()
print(solve.largestRectangleArea_dandiao([2,1,5,6,2,3]))