# 编写一个函数 输入的是一个无符号整数 返回其二进制表达式中数字为1的位的个数
# 因为是按位与 所以必须两个都是1 所得才不是0
# 比如 111...11 和000...01检测最后一位
# 左移一位后变成了 111..11和000..10检测倒数第二位
class Solution:
    def hammingWeight(self, n:int)->int:
        retval = 0
        for i in range(32):
            if n & (1 << i):
                print(n & (1 << i))
                print(1<<i)
                retval += 1
        return retval
    # 对于任意的整数都需要执行32次移位和与操作 如果整数比较小那么这些操作就是多余的。
    # 因此可以依次讲最低位且值为1的比特位翻转为0 并且增加计数器 当执行结果导致整数=0时，就不会再含有任何为1的比特了
    # 翻转最低有效比特为1的比特为0 可以通过n&(n-1)完成 因为最低有效比特为1的位置 对应的n-1中一定是0 比如 111111100 111111011
    def hammingWeight_flip(self,n:int)->int:
        retval = 0
        while n:
            retval = retval+1
            n &= (n-1)
        return retval

solve = Solution()
n = 11111111111111111111111111111111
answer = solve.hammingWeight(n)
print(answer)
