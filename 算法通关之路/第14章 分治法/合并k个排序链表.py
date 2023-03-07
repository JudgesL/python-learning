from typing import List
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self,lists:List[ListNode])->ListNode:
        def mergeTwoLists(l1:ListNode,l2:ListNode):
            sentinel = ListNode(-1)
            curr = sentinel
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 is not None else l2

            return sentinel.next

        if not lists:
            return None
        l =lists[0]
        for i in range(1,len(lists)):
            mergeTwoLists(l,lists[i])
        return l
    # 分治法
    # 可以发现在最后一个循环里 list0反复被比较 具体来说，其被比较了k-1次 list1被比较了k-2次
    # 但是这是可以被避免的。 只需要两两进行合并，问题就能对半减少
    def mergeKLists_fenzhi(self,lists:List[ListNode])->ListNode:
        def mergeTwoLists(l1:ListNode,l2:ListNode):
            sentinel = ListNode(-1)
            curr = sentinel
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 is not None else l2

            return sentinel.next

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0,amount - interval, interval*2):
                lists[i] = mergeTwoLists(lists[i],lists[i+interval])
            interval *= 2
        return lists[0] if amount>0 else lists
