# 两个容量分别是x和y的水壶 判断能否通过这两个水壶 得到恰好z升水
# 6种行动 x空 y空 x满 y满 x给y y给x
# 每种行动都可能产生一种情况 如果已经发现过就不用深入 如果是新的就继续在这个基础上继续
class Solution:
    def canMeasureWater(self,x:int,y:int,z:int)->bool:
        if x+y < z:
            return False
        queue = [(0,0)]
        seen = set((0,0))
        # 还有新发现的状态没有处理完
        while len(queue) > 0:
            a,b = queue.pop(0)
            if a==z or b==z or a+b == z:
                return True
            # 寻找新的可能性
            states = set()
            # x装满
            states.add((x,b))
            # y装满
            states.add((a,y))
            # x空
            states.add((0,b))
            # y空
            states.add((a,0))
            # y给x
            states.add((min(x,a+b),0 if b<x-a else b-(x-a)))
            # x给y
            states.add((0 if a<y-b else a-(y-b),min(y,a+b)))
            for state in states:
                if state in seen:
                    continue
                else:
                    queue.append(state)
                    seen.add(state)
        return False

    # 裴蜀定理 当且仅当k是d的倍数时 mp+nq=k有解 其中d为p和q的最大公约数。
    # 也就是说只要z是x和y的最大公约数的倍数 就可以
    def canMeasureWater(self,x:int,y:int,z:int)->bool:
        if x+y <z:
            return False
        if z==0:
            return True
        if x==0:
            return y==z
        if y==0:
            return x==z

        def GCD(a:int,b:int)->int:
            smaller = min(a,b)
            while smaller:
                if a%smaller ==0 and b%smaller == 0:
                    return smaller
                smaller -= 1
        def GCD_better(a:int,b:int)->int:
            return a if b==0 else GCD(b,a%b)


