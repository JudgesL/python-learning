# 设计一个支持push、pop、top操作，并且能在常数时间内检索到最小元素的栈
class MinStack:
    def __init__(self):
        '''
        initialize your data strcture here
        '''
        self.stack = []
        self.helper = []
    def push(self,x:int)->None:
        self.stack.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self)->None:
        self.helper.pop()
        return self.stack.pop()

    def top(self) ->int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]

# 改进辅助栈，在保存的时候把最小值合并成一个组合[value,count]
class MinStack_v1:
    def __init__(self):
        '''
        initialize your data strcture here
        '''
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.helper or x <= self.helper[-1][0]:
            self.helper.append([x,1])
        else:
            self.helper[-1] = [self.helper[-1][0],self.helper[-1][1]+1]

    def pop(self) -> None:
        if self.helper[-1][1]>1:
            self.helper[-1] = [self.helper[-1][0],self.helper[-1][1] - 1]
        else:
            self.helper.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1][0]

# 再次改进 只有当插入的值小于或等于辅助栈顶的值 才进行插入 pop时仅当stack栈顶=helper栈顶时 才pop
class MinStack_v2:
    def __init__(self):
        '''
        initialize your data strcture here
        '''
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        top = self.stack.pop()
        if self.helper and top == self.helper[-1]:
            self.helper.pop()
        return top

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]

# 不使用辅助栈 使用一个min变量存储当前值和最小值的差值、、或者用min存储最小值 把差值存入栈 这里实现的是后一种
class MinStack_v3:
    def __init__(self):
        '''
        initialize your data strcture here
        '''
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        if not self.stack:
            self.min = x
            self.stack.append(0)
        else:
            self.stack.append(x - self.min)
            if x < self.min: self.min = x

    def pop(self) -> None:
        if not self.stack:return

        top = self.stack.pop()
        if top < 0:
            self.min = self.min - top

    def top(self) -> int:
        top = self.stack[-1]
        if top<0: return self.min

        return top + self.min

    def getMin(self) -> int:
        return self.min