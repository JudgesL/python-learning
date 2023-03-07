# 如果a是b的朋友，b是c的朋友，那么可以认为a和c也是朋友
# 查找班级的朋友圈
from typing import List
class UnionFind:
    def __init__(self,n:int):
        # 每个结点的父结点
        self.parent = [i for i in range(n)]
        # 以该结点为根的树权（节点数）
        self.rank = [0 for i in range(n)]
        # 连通区域数量
        self.cnt = n

    def find(self,p:int)->int:
        # 这个过程在查找结点的始源 祖先结点 如果p=parent[p] 那代表是孤独的
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def find_optimize(self,p:int)->int:
        # 可以把每个子支在查找的时候顺便把父节点指向祖先
        if p!= self.parent[p]:
            self.parent[p] = self.find_optimize(self.parent[p])
        return self.parent[p]

    def union(self,p:int,q:int):
        root_p,root_q = self.find(p),self.find(q)
        if root_p == root_q:
            # 代表有同一个祖先 是连通的
            return
        # 这边在比较祖先结点的树权 把小的合到大的
        if self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        elif self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        else:
            # 如果是两个同等大小的在合并 那么随便合一个 并且增加树权来区分
            self.parent[root_q] = root_p
            self.rank[root_p] += 1
        # 连通域减少了
        self.cnt -= 1