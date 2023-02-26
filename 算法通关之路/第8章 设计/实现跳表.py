#设计跳表 详细描述见书p153
# randomLevel() 返回1表示不需要建立索引 返回2表示建立1级索引 返回3表示建立1、2级索引 以此类推
from typing import Optional
import random
# 在你提供的例子中，Optional[int] 表示该变量或函数参数可以是一个整数或者是 None。
# 如果在类型注解中没有使用 Optional，那么该变量或函数参数只能是一个整数类型。
# 使用 Optional 类型注解的好处是可以让代码更加明确和类型安全。
# 如果你尝试将一个非整数类型的值赋给一个带有 Optional[int] 类型注解的变量，
# 或者将一个整数类型的值传递给一个带有 Optional[int] 类型注解的函数参数时，Python 解释器会在运行时抛出一个类型错误。
class ListNode:
    def __init__(self, data:Optional[int] = None):
        self._data = data # 链表节点的数据域，可以为空（创建头结点）
        self._forwards = [] #存储各索引阶级中该节点的后驱节点

class Skiplist:

    _MAX_LEVEL = 16 #允许的最高索引高度

    def __init__(self):
        self._level_count = 1 # 初始化当前阶级为1
        self._head = ListNode()
        self._head._forwards = [None]*self._MAX_LEVEL

    def search(self,target:int)->bool:
        p = self._head
        # 从最高索引阶级不断搜索 如果当前没有 就可以下沉到第一层的阶级
        for i in range(self._level_count-1, -1, -1):
            # 等到出现索引中有>的，就跳到下一个阶级
            while p._forwards[i] and p._forwards[i]._data < target:
                p = p._forwards[i]

        if p._forwards[0] and p._forwards[0].data == target:
            return True

        return False

    def _random_level(self,p:float = 0.5)->int:
        level = 1
        while random.random() < p and level < self._MAX_LEVEL:
            level += 1
        return level

    def add(self,num:int)->None:
        # 随机生成索引阶级
        level = self._random_level()
        if self._level_count < level:
            # 更新最高阶级
            self._level_count = level
        new_node = ListNode(num)
        new_node._forwards = [None]*level
        # 保存各个索引阶级插入的位置 也就是新节点的前驱
        update = [self._head]*self._level_count
        p = self._head
        # 用一段代码获取新插入节点在各个索引阶级的前驱节点
        # 这里用了最高层级进行循环
        for i in range(self._level_count -1,-1,-1):
            while p._forwards[i] and p._forwards[i]._data < num:
                # 把p切换成了这个层级上的后继节点 完成了p的后继
                p = p._forwards[i]
            # 找到了该层的插入位置
            update[i] = p

        # 更新索引阶级
        for i in range(level):# 更新需要更新的各个阶级
            # 新结点的后继设置为 update[i]插入位置 同层的后继forwards[i]
            new_node._forwards[i] = update[i]._forwards[i]
            # 更新新节点的前一个结点 其后置需要设置为新节点
            update[i]._forwards[i] = new_node

    def erase(self,num:int)->bool:
        update = [None]*self._level_count
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < num:
                # 把p切换成了这个层级上的后继节点 完成了p的后继
                p = p._forwards[i]
            # 找到了该层的删除位置
            update[i] = p

        # 如果真的能找到
        if p._forwards[0] and p._forwards[0]._data == num:
            for i in range(self._level_count-1,-1,-1):
                # 对上层全部索引做修改
                if update[i]._forwards[i] and update[i]._forwards[i]._data == num:
                    # 跳过删除的那个
                    update[i]._forwards[i] = update[i]._forwards[i]._forwards[i]
            return True

        # 更新全局最高层
        while self._level_count > 1 and not self._head._forwards[self._level_count]:
            self._level_count -= 1

        return False








