class Node:
    def __init__(self, index):
        self.index = index       # 노드의 고유 인덱스
        self.father = None       # 부모 노드
        self.son = set({})            # 자식 노드 리스트
        self.key = 1

class LinkedList:
    def __init__(self):
        self.nodes = {} 
    def add_node(self, index):
        if index not in self.nodes:
            self.nodes[index] = Node(index)

    def sfather(self, node_index, parent_index):
        node = self.nodes[node_index]
        parent_node = self.nodes[parent_index]
        
        node.father = parent_node
        parent_node.son.add(node.index)  # 부모의 자식 리스트에 현재 노드 추가
        parent_node.key=0

        # 재귀적으로 조부모의 자식 리스트 업데이트
        self.update_ancestor_son_lists(parent_node, node.index)

    def update_ancestor_son_lists(self, node, child_index):

        if node.father is not None:  # 부모가 존재한다면
            node.father.son.add(child_index)  # 부모의 부모의 자식 리스트에 추가
            node.father.key=0
            self.update_ancestor_son_lists(node.father, child_index)  # 재귀 호출
        
number=int(input())
numberlist=list(map(int,input().split()))
numberlist=[(index,value) for index,value in enumerate(numberlist)]
number2=int(input())
# 연결 리스트 생성
linkedlist_instance = LinkedList()

# 노드 추가
for i in numberlist:
    linkedlist_instance.add_node(i[0])
for i in numberlist:
    if i[1]==-1:
        root=i[0]
        pass
    else:
        linkedlist_instance.sfather(i[0],i[1])
for i in numberlist:
    if i[1]==-1:
        root=i[0]
        pass
    else:
        linkedlist_instance.sfather(i[0],i[1])
sum=0
# 출력 확인
if root==number2:
    print(sum)
elif len(linkedlist_instance.nodes[number2].father.son)-len(linkedlist_instance.nodes[number2].son)==1:
    sum=sum+1
    total=set(linkedlist_instance.nodes[root].son)-{number2}
    erase=set(linkedlist_instance.nodes[number2].son)
    for i in total-erase:
        sum=sum+linkedlist_instance.nodes[i].key
    print(sum)
else:
    total=set(linkedlist_instance.nodes[root].son)-{number2}
    erase=set(linkedlist_instance.nodes[number2].son)
    for i in total-erase:
        sum=sum+linkedlist_instance.nodes[i].key
    print(sum)