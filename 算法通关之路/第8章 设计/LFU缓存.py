# 设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作 get和put
# get(key) 如果key存在于缓存中，获取秘钥的值，否则返回-1.值总是正数
# 写入数据put(key,value) 如果秘钥不存在 就写入数据值 缓存达到上限时，删除最不常用的项目 平局就删除最近使用最少的那个
# 这里设计了两个哈希表 一个node哈希表和之前一样 一个freq哈希表其中每个key对应一个双向链表
# 设计DLinkedList是为了把访问次数相同的结点都放到一起 方便删除

import collections

class Node:
    def __init__(self,key:int,val:int):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        # 哨兵结点 是头结点的前驱和尾结点的后继
        self._sentinel = Node(None,None)
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self,node:None):
        # 插入的node作为头结点 其next是原本的头结点。也就是哨兵的next
        node.next = self._sentinel.next
        # 插入的node作为头结点 其prev是哨兵
        node.prev = self._sentinel
        # 原本的头结点的prev需要改成node
        node.next.prev = node
        # 哨兵的next需要改成node
        self._sentinel.next = node
        self._size += 1

    def remove(self,node:Node):
        # 如果node不存在，直接返回
        if not node:
            return
        # 将node从链表中移除
        node.prev.next = node.next
        node.next.prev = node.prev
        # 将node的前驱和后继指针设为None，防止引用了已经删除的节点
        node.prev = None
        node.next = None
        self._size -= 1

    def pop(self,node:Node=None) -> Node:
        # 如果链表为空，直接返回None
        if self._size == 0:
            return None
        # 如果未指定node，则删除尾节点
        if not node:
            node = self._sentinel.prev
        self.remove(node)
        return node

class LFUCache:
    def __init__(self, capacity:int):
        # _在python中约定俗成的表示这是一个私有变量 尽量不要直接访问他
        #dict()和{}都是创建普通字典，没有默认值，只是构造方法不同。
        # defaultdict在创建时需要传递一个参数作为默认值，当访问不存在的键时，会返回这个默认值。可以使用默认值对字典进行计数等操作，而不需要使用if判断键是否存在并设置默认值。
        # 当使用dict()和{}时，如果访问一个不存在的键，会抛出KeyError异常。而当使用defaultdict时，访问不存在的键时，会返回默认值。这是一个主要区别。
        # 总之，dict()和{}是用于创建普通字典的，而defaultdict是一种特殊的字典，它可以自动设置默认值。
        self._size = 0
        self._capacity = capacity
        self._node = dict()
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0

    def _update(self, node:Node):
        # 这里主要用于node被访问以后 被访问次数+1 导致需要从对应的DKLinkedList中转移 并且更新全局最小值
        freq = node.freq
        self._freq[freq].pop(node)
        # 更新全局最小
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self,key:int)->int:
        if key not in self._node:
            return -1

        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key:int,value:int)->None:
        if self._capacity == 0:
            return

        #key已经存在只需要更新val 并且这个也是一次访问
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                # 从双向链表中删除
                node = self._freq[self._minfreq].pop()
                # 从哈希表中删除
                del self._node[node.key]
                self._size -= 1
            #删除或不需要删除后 需要创建这个新结点
            node =Node(key,value)
            # 放入哈希表
            self._node[key] = node
            # 放入双向链表
            self._freq[1].append(node)
            # 更新全局最小
            self._minfreq = 1
            self._size += 1




