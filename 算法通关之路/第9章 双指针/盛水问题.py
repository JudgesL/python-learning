# 给定n个非负整数 a1,a2,...,ab 每个数代表坐标系中的一个点（i,ai)。在坐标系中画n条垂直线 垂直线i的两个断线分别为（i,ai)和(i,0)
# 找出其中两根线，使他们与x轴共同构成的容器可以容纳最多的水

from typing import List
class Solution:
    #暴力法
    def maxArea(self,height:List[int])->int:
        res, area = 0, 0
        for i in range(0,len(height),1):
            for j in range(i+1,len(height),1):
                area = (j-i)*min(height[j],height[i])
                if area > res :
                    res = area
        return res
    # 双指针法
    # 由于水池的两个板的储水面积是由最矮的板决定的
    # 假设a[i+n] 比a[i-j]小，那么如果最大值不是a[i+n]与a[i-j] 那么只可能是数组在a[i-j]与a[i+n-1]的值
    # 因为对于较小的板a[i+n]，任何值都无法超过其与a[i-j]的组合。
    def maxArea_shuangzhizhen(self,height:List[int])->int:
        left,right,width,res =0,len(height)-1,len(height)-1,0
        # 面积递减 因为左右指针都会改变 其实也就是while left<right
        for w in range(width,0,-1):
            if height[left] < height[right]:
                # 最大值出现在当前 或者就是left+1,right之间
                res, left = max(res,height[left]*w),left+1
            else:
                res,right = max(res,height[right]*w),right-1

        return res


