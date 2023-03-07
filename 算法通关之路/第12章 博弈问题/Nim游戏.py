# 桌面上有一堆石子 轮流拿掉1-3块 拿掉最后一块石子的就是获胜者
# 石头剩下1-3 直接获胜 石头剩下4 必输 石头剩下5 必胜
class Solution:
    def canWinNim(self,n:int)->bool:
        mem = [True]*(n+1)
        for i in range(4,n+1):
            # mem[i-1] [i-2][i-3]代表了取石头之后的情况 这意味着 如果这几个都是可胜利 那就会导致对手胜利
            # 所以如果满足这个条件 就是False（输） 否则是True（我方胜利）
            if not (mem[i-1] and mem[i-2] and mem[i-3]):
                mem[i] = True
            else:
                mem[i] = False
            print('i=',i)
            print('mem=',mem[i])
        return mem[n]
    # 不需要全部存储
    def canWinNim(self,n:int)->bool:
        if n<4:
            return True
        a,b,c=True,True,True
        for i in range(4,n+1):
            current = not (a and b and c)
            a,b,c = b,c,current
        return c
    
solve = Solution()
solve.canWinNim(10)