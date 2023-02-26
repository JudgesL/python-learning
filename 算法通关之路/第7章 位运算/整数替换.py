# 给定一个正整数：如果n是偶数 用n/2替换n
# 如果n是奇数，可以用n+1或n-1替换n 计算n变为1所需的最小替换次数是多少
class Solution:
    def integerReplacement(self,n:int)->int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return 1 + self.integerReplacement(n//2)
        else:
            return 1+min(self.integerReplacement(n+1),self.integerReplacement(n-1))
        #用位的角度去分析 如果n是偶数 直接n/2 如果n是奇数考虑如下情况
        # 二进制码后两位是01 则n-1
        # 二进制码后两位是11 则n+1
        # 特殊情况n=3 即只有后两位 且是11 这个时候令其-1
    def integerReplacement_bin(self,n:int)->int:
        if (n<=1):
            return 0
        count = 0

        while n > 3:
            # 判断n为偶数
            if n & 1 == 0:
                n >>= 1
            # n为奇数的时候 判断后两位情况
            # 0x03就是 11 如果&0x03=0x03 那么后两位就是11
            elif n & 0x03 == 0x03:
                n += 1
            else:
                n -= 1
            count += 1
        # 对问题进行收尾 如果在3停止就+2 否则+1
        return (count+2) if (n==3) else (count+1);

    def integerReplacement_bin2(self, n:int)->int:
        count = 0
        # 可以把n=3的时候的相减 和 n最后两位为01合并
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            else:
                if (n&2) == 0 or n == 3:
                    n += -1
                else:
                    n += 1
            count += 1
        return count