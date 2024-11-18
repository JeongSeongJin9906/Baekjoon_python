import sys
sys.setrecursionlimit(100100)
class Node:
    def __init__(self,index):
        self.index=index
        self.linkes=set()
        self.father=None
class Linkednodes:
    def __init__(self):
        self.nodes={}
    def make_link(self,node1,node2):
        if node1 not in self.nodes:
            self.nodes[node1] = Node(node1)
        if node2 not in self.nodes:
            self.nodes[node2] = Node(node2)
        currentnode1=self.nodes[node1]
        currentnode2=self.nodes[node2]
        currentnode1.linkes.add(currentnode2)
        currentnode2.linkes.add(currentnode1)
    def make_father(self,index):
        stack = [self.nodes[index]]  # Stack으로 DFS 구현
        while stack:
            currentnode = stack.pop()
            for i in list(currentnode.linkes):
                if i.father is None:
                    i.father = currentnode
                    currentnode.linkes.remove(i)
                    i.linkes.remove(currentnode)
                    stack.append(i)
link=Linkednodes()
number=int(input())
for i in range(number-1):
    a,b=tuple(map(int,input().split()))
    link.make_link(a,b)
link.make_father(1)
for i in range(2,number+1):
    if link.nodes[i].father!=None:
        print(link.nodes[i].father.index)