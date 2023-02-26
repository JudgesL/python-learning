# 实现int sqrt(int) 函数 计算并返回x的平方根 x是非负整数
# 由于左边界向下取整更新为mid的时候 有可能产生死循环 在查找范围只有两个元素的时候可以直接退出循环
# 如果更新左边界 例如左右1 2 的时候 因为是向下取整 因此左边界无论如何更新都会是1 这样查找范围不缩小就会导致死循环
# 如果更新右边界 例如左右1 2 的时候 因为是向下取整 因此右边界更新以后变成了1 这样查找范围肯定会缩小 不会死循环
# 这样两种情况都只会发生在不确定性的二分查找中
class Solution:
    def mySqrt(self, x:int) -> int:
        l ,h = 0,x
        while l<= h:
            mid = l + (h-l)//2
            if l == h or l+1 == h:
                break
            elif mid * mid > x:
                h = mid - 1
            else:
                l = mid
        if h*h <= x:
            return h
        else:
            return l


