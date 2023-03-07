# 给定一个数组 将数组中的元素向右移动k个位置 k为非负数
from typing import List
class Solution:
    def rotate(self,nums:List[int],k:int)->None:
        # 直接复制一份数组 这样就可以原地旋转了 从复制的数组取数即可
        copy = nums.copy()
        n = len(nums)
        if k% n == 0:
            return
        for i in range(n):
            nums[(k+i)%n] = copy[i]

    # 时间换空间 每次只移动1位 这样只需要1个额外的空间就可以了
    def rotate_timetospace(self,nums:List[int],k:int)->None:
        n = len(nums)
        t = None
        # 右移k位 和 左移n-k是完全等效的
        offset = n - k%n
        while offset:
            t = nums[0]
            offset -= 1
            for i in range(n-1):
                # 集体左移
                nums[i] = nums[i+1]
            nums[n-1] = t

    # 空间换时间 把数组完完全全复制一份贴在原数组后面 然后这样移动问题就变成了截取问题
    def rotate_paste(self,nums:List[int],k:int)->List[int]:
        n = len(nums)
        offset = k%n
        nums = nums + nums.copy()
        return nums[n-offset:n+n-offset]

    def rotate_three(self,nums:List[int],k:int)->List[int]:
        def reverse(list:List[int],start:int,end:int)->None:
            # 不断首尾交换
            while start < end:
                t = list[start]
                list[start] = list[end]
                list[end] = t
                start += 1
                end -= 1
        n = len(nums)
        offset = k % n
        if offset == 0:
            return
        reverse(nums,0,n-offset-1)
        reverse(nums,n-offset-1,n-1)
        reverse(nums,0,n-1)