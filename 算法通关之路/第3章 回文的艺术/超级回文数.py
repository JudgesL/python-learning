# 如果一个正整数自身是回文数 而且它也是另一个回文数的平方 那我们称其为超级回文数
# 1<=len(L）<=18 R同样
# 暴力法
import math
class Solution:
    def superpalidromesInRange(self,L:str,R:str)->int:
        cnt = 0
        # 判断回文数
        def validPalindrome(s:str)-> bool:
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
                return True
        # 在math.floor(sqrt(L)) 到 math.ceil(sqrt(R))之间寻找即可
        for i in range(math.floor(int(L)**0.5), math.ceil(int(R)**0.5)):
            if validPalindrome(str(i)) and validPalindrome(str(i**2)):
                cnt += 1
        return cnt
    # 但是实际上不需要遍历那么多数 因为有的数本身就不是回文数了 更不用判断它的平方
    # 因此可以通过 构造回文数 然后查询构造出的回文数是否满足平方回文即可
    # 构造的时候可以将回文数分为前后两段 将前段重复一次就可以得到回文 比如32123 321123两种
    def superpalidromesInRange_gouzao(self,L:str,R:str)->int:
        cnt = 0
        i = 1
        seen = {}
        # 判断回文数
        def validPalindrome(s:str)-> bool:
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
                return True
        while i <10**5:
            #log10防止出现精度丢失的问题
            power = math.floor(math.log10(i))
            x = i
            r = 0
            while x > 0:
                r = r*10 + (x%10)
                x = x//10
            # 比如123*100+321%100 = 12321
            # r % (10**power) 其实是去掉r的最高位
            Q = (i*10**power + r % (10**power))**2
            if Q > int(R):
                return cnt
            if Q >= int(L) and validPalindrome(str(Q)):
                # 避免重复
                if Q not in seen:
                    cnt += 1
                    seen[Q] = True
            # 比如123321
            Q = (i*10**(power+1) + r)**2
            if Q >= int(L) and Q <= int(R) and validPalindrome(str(Q)):
                if Q not in seen:
                    cnt += 1
                    seen[Q] = True
            i += 1
        return cnt