# 给定一个数组nums 有一个大小为k的滑动窗口从数组最左侧移动到数组最右侧 只可以看到滑动窗口中的k个数字 滑动窗口每次只向右移动一位 返回窗口中最大值
# 显而易见的是 如果每次移动窗口都要全部进行一次排序 那复杂度会非常高
# 如果记录窗口中的的最大值 每次和滑动的新元素比较 但又遇到了左边的元素会不会是最大值 有没有被移出的问题
import collections
import sys
from typing import List
from collections import deque
class Solution:
    # 暴力法
    def maxSlidingWindow(self,nums:List[int],k:int)->List[int]:
        length = len(nums)
        if length*k == 0:
            return []
        output = []
        # 遍历所有可能的窗口
        for i in range(length - k + 1):
            max_val = -sys.maxsize - 1
            for j in range(i,i+k):
                max_val = max(max_val,nums[j])
            output.append(max_val)
        return output

    # 滑动窗口法
    # 当有元素加入时 窗口左侧的所有元素 和窗口内所有比新加入的元素更小的元素 将不再对结果产生影响
    # 需要一个可以删除窗口左侧元素 添加新元素的数据结构 选择双端队列
    # 双端队列保存元素的索引而非元素本身 因为有可能有重复的元素值
    def maxSlidingWindow_window(self,nums:List[int],k:int)->List[int]:
        # double-ended queue
        d = collections.deque()
        out = []
        #enumerate() 函数返回一个可迭代的对象，其中每个元素都是一个元组，包含当前迭代的索引和对应的值。
        for i,n in enumerate(nums):
            # 从尾部移出比新加入元素更小的元素
            while d and nums[d[-1]] < n:
                d.pop()
            # 新加入的元素放在尾部
            #deque 可以使用 += 运算符添加新的元素。具体来说，+= 运算符会将另一个可迭代对象中的元素添加到 deque 的右侧，
            # 就像使用 extend() 方法一样。
            d += i,
            print(d)
            # 如果窗口外的元素仍然在双端队列中 移出
            if d[0] == i-k:
                d.popleft()
            # 头部就是最大值
            if i >= k-1:
                out.append(nums[d[0]])
        return out



