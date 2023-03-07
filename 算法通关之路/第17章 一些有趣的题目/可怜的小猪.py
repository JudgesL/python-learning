#小猪喝水 找毒水
# 如果小猪中毒后15min死亡 一小时时间 那它能检测多少桶水？ 5桶
# 如果两头小猪呢 事实上 25桶 检测4行4列 如果有对应死亡 就必定锁定位置 如果没死 就是唯一的25号
import math


class Solution:
    def poorPigs(self,buckets:int,minutesToDie:int,minutesToTest:int)->int:
        cnt = 0
        while (minutesToTest/minutesToDie +1)**cnt < buckets:
            cnt += 1
        return cnt
    # 第二种方法 我们假设只有15分钟的测试时间 可以通过将1000个桶用二进制去编号
    # 每头猪用来确定一个bit位上的值 比如1024是10位，每头猪喝的水都有一个特点，那就是其对应序号上的二进制值都是一样的
    # 也就是第一头喝的都是第一位0或者第一位1的水 这样十头猪喝完结果就被唯一确定了
    # 这是二分法精神的体现 每次喝完必定导致结果缩小一半（一个位被确定）

    # 当我们的测试时间延长 实质上小猪被赋予了更多的状态 从生 死，变成了第一次死，第二次死，第三次死，第四次死，一直活着。
    # 所以x只s状态的猪 检测出了s^x种状态。
    def poorPigs_two(self,buckets:int,minutesToDie:int,minutesToTest:int)->int:
        return math.ceil(math.log(buckets,minutesToTest/minutesToDie + 1))

solve = Solution()
print(solve.poorPigs(1000,15,60))
print(solve.poorPigs_two(1000,15,60))