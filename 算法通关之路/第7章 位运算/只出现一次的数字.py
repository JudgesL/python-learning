# 给定一个非空整数数组 除某个元素只出现1次外 其余每个元素均出现2次 找出那个只出现1次的元素
from typing import List
from collections import defaultdict
# 使用defaultdict(int)和mapper={}创建哈希表的主要区别在于当访问一个不存在的键时的行为不同。
#
# 当使用mapper={}创建哈希表时，如果访问一个不存在的键，则会抛出KeyError异常。为了避免这种情况，我们需要使用if key in mapper进行判断，或者使用mapper.get(key, default_value)方法获取默认值。
#
# 而使用defaultdict(int)创建哈希表时，如果访问一个不存在的键，会自动创建一个键值对，其默认值为0。因此，我们可以直接访问哈希表中的任何键，无需进行额外的判断或处理。
#
# 另外，defaultdict(int)还有一个好处是可以在创建哈希表时指定默认值类型，这样在访问不存在的键时会自动创建一个默认类型的对象。而使用mapper={}创建哈希表时，默认值类型只能是None。
#
# 综上所述，使用defaultdict(int)可以更方便地创建和访问哈希表，避免了一些额外的判断和处理。
class Solution:
    # 哈希表法
    def singleNumber(self,nums:List[int])->int:
        hash_lab = defaultdict(int)

        for i in nums:
            hash_lab[i] += 1

        for i in hash_lab:
            if hash_lab[i] == 1:
                return i
    # 异或法：
    # 因为如果一个数字出现了两次，那么它们异或的结果为0。因此，如果我们将整个数组中的所有数字都异或起来，最后的结果就是只出现1次的元素。
    # 因为异或运算满足交换律和结合律，所以遍历数组的顺序并不影响最终结果。
    def singleNumber_yihuo(self,nums:List[int])->int:
        ret = 0

        for i in range(len(nums)):
            ret ^= nums[i]

        return ret
    # 数学法：
    # 假设数组有a a b b c 几个元素，那么2*(a+b+c)-(a+a+b+b+c)=c
    def singleNumber_math(self,nums:List[int])->int:
        return 2*sum(set(nums)) - sum(nums)

    # 如果题目改成出现每个元素出现3次 那么哈希法 数学法都还是可以使用 但是异或法不能再使用了
    # 但是对于出现了三次的元素 那么它二进制形式中每一位都是3的倍数 只需要统计在二进制形式中1出现的次数即可。
    # 在这个问题中，我们要找到只出现1次的元素，该元素在数组中出现了3次。如果数组中的元素都是正整数，则我们可以使用位运算来解决这个问题。在代码中，
    # 我们用counts数组记录了每一位上1的个数，然后对每一位上1的个数取余数，得到只出现1次的元素在该位上的值。最后，将所有位上的值组合起来，就得到了只出现1次的元素。
    # 在计算结果时，我们需要考虑两种情况：只出现1次的元素是正数或负数。如果只出现1次的元素是正数，则直接将结果返回即可。
    # 但如果只出现1次的元素是负数，则需要对结果进行处理，以得到正确的负数表示。
    # 具体地，如果只出现1次的元素是负数，它在二进制中的表示是最高位为1的数。在对每一位上1的个数取余后，
    # 得到的结果是该位上只出现1次的元素的值。因此，最高位上的余数应该为1，表示只出现1次的元素是负数。此时，我们需要将结果转换为有符号整数，
    # 并返回正确的负数结果。
    # 在这个问题中，如果res的值为0b11111111111111111111111111101101，则res ^ 0xffffffff的结果应该是
    # 0b00000000000000000000000000010010，
    # 而~(res ^ 0xffffffff)的结果应该是 - 0b00000000000000000000000000010011，
    # 即对res ^ 0xffffffff的每一位取反得到的结果再加上符号位。
    def singleNumber_three(self, nums:List[int])->int:
        counts = [0]*32
        for num in nums:
            for j in range(32):
                counts[j] += num&1
                num >>= 1
        res,m = 0,3
        # 对每一位上统计的1的个数取余
        for i in range(32):
            res <<= 1
            print(bin(res))
            # |= 是按位 或
            res |= counts[31-i] % m
        #res ^ 0xffffffff表示逐位取反
        if counts[31] % m !=0:
            print('res:',bin(res))
            print('res=',res)
            print('res ^ 0xffffffff',bin(res ^ 0xffffffff))
            print('~(res ^ 0xffffffff)',bin(~(res ^ 0xffffffff)))
        # 正数的补码，是其本身；
        # 负数的补码，就用它的正数，减一取反，即可得到补码。
        # 在Python中：将正数 / 负数和0xffffffff相与，即可得到其补码形式。
        # 补码中，第一位符号位0正，1负；
        # 所以可将补码与0x7fffffff（第一位0，其余1）进行比较， <= 0x7fffffff
        # 为正数，否则为负数。
        # 负数补码num想要恢复为正常数字，需要进行~(num ^ 0xffffffff)操作
        # 解释：（num ^ 0xffffffff(异或运算)
        # 按位取反，~ 整体取反）
        # 说白了 如果是负数 res一开始就是这个答案。但是需要把用补码表示的负数转换成有符号的负数 所以就用~(res ^ 0xffffffff)就行
        return res if counts[31] % m ==0 else ~(res ^ 0xffffffff)

    def singleNumber_three_simple(self, nums:List[int])->int:
        one,two =0,0
        for num in nums:
            print('now the num is:',bin(num))
            # two的相应位等于1 相当于该位出现2次
            two |= (one & num)
            print('two:',bin(two))
            # one的相应位等于1 相当于该位出现1次
            one ^= num
            print('one:',bin(one))
            # three的相应位等于1 表示该位出现3次
            three = (one & two)
            print('three:', bin(three))
            # 如果相应的位出现3次 把改位置0
            two &= ~three
            one &= ~three
        return one
    # 继续修改题目，给定一个整数数组nums,其中恰好有两个元素只出现1次 其余所有元素都出现2次 找出只出现1次的2个元素
    # 对全员进行异或 这样得到的结果就是两个独特数的异或答案 因为其他数都被抵消了
    # 接下来进行分组 根据异或结果为1的那一位的情况。必定会有最少1位是1 因为不然的话就会完全相同
    # 在异或为1的那个位上 两个独特的数的各自是0,1。因此把所有的数分到两类，0和0一起，1和1一起。那么独特数必定分到两边
    # 两组各自异或的结果就是答案
    def singleNumber_change(self,nums:List[int])->List[int]:
        ret = 0
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        # 找到是1的位
        h = 1
        while ret&h == 0:
            h <<= 1
        for n in nums:
            if h & n == 0:
                a ^= n
            else:
                b ^= n
        return [a,b]

solve = Solution()
nums = [1,1,1,2,2,2,19]
answer = solve.singleNumber_three_simple(nums)
print(answer)
print(bin(answer))



