# 提供分子分母 要求将分数转化为小数 如果是循环小数 将循环部分放在括号内
# 难度在于如何找出小数的循环部分
# 以2/3举例，先由分子除分母，如果为0直接返回，如果不为0，保留余数*10 再继续除 可以见到分子将会连续出现20 于是确定了循环节
from typing import List
class Solution:
    def fractionToDecimal(self,numerator:int, denominator:int)->str:
        # 长除法
        n, remainder = divmod(abs(numerator),abs(denominator))
        sign = ''
        if (numerator//denominator < 0):
            sign = '-'
        res = [str(n), '.']
        seen = []
        while(remainder not in seen):
            seen.append(remainder)
            n,remainder = divmod(remainder*10, abs(denominator))
            res.append(str(n))
        # 如果找到了循环重复部分，就会脱离while
        index = seen.index(remainder)
        # 因为res中多了第一位和'.'，所以需要+2
        res.insert(index+2,'(')
        res.insert(')')
        # 如果没有小数 可以整除 那需要去掉'.' 最后一位为0可以整除以后也会导致出现循环(0)
        return sign+''.join(res).replace('(0)','').rstrip('.')