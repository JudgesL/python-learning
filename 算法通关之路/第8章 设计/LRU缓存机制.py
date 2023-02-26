# 设计和实现一个LRU（最近最少使用）缓存机制
# get(key) 如果key存在于缓存中，获取秘钥的值，否则返回-1.值总是正数
# 写入数据put(key,value) 如果秘钥不存在 就写入数据值 缓存达到上限时，删除最新最少使用的数据值
# 在O(1)的时间里获取到对应的值 因此可以使用哈希表 要删除最近最少使用的数据值 那需要用到双向链表
class ListNode:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建头尾结点
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表
        self.head.next = self.tail
        self.tail.prev = self.head

    # 在使用get 和 put的操作都有可能用到move_to_tail
    def move_to_tail(self,key:int)->int:
        # 用hashmap[key]需要保证这个值一定在hashmap中 否则会报错
        node = self.hashmap[key]
        # 前后结点相连
        node.prev.next = node.next
        # node的prev 和 next
        node.prev = self.tail.prev
        node.next = self.tail
        # 原本的末节点和tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self,key:int)->int:
        if key in self.hashmap:
            # 如果node已经存在链表中 这次调用将导致它被移到尾结点
            self.move_to_tail(key)
            return self.hashmap.get(key).value
        #如果不存在 返回-1
        return -1

    def put(self,key:int,value:int)->None:
        # 如果已经存在 只需要更新该值对应的value
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 从哈希表中移出
                self.hashmap.pop(self.head.next.key)
                # 从链表中移出
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 插入新结点
            newNode = ListNode(key,value)
            self.hashmap[key] = newNode
            newNode.prev = self.tail.prev
            newNode.next = self.tail
            self.tail.prev.next = newNode
            self.tail.prev = newNode

