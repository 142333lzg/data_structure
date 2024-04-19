class binary_tree():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = binary_tree("a")
b = binary_tree("b")
c = binary_tree("c")
d = binary_tree("d")
e = binary_tree("e")
f = binary_tree("f")
g = binary_tree("g")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

def pre_order(root): # 前序遍历
    if root: # 判断 root 是否存在
        print(root.data, end='')
        pre_order(root.lchild)
        pre_order(root.rchild)

# 用迭代实现递归（栈）：
def pre_order_iter(root):
    li = [root]
    while len(li) > 0:
        cur = li[-1]
        print(cur.data, end='')
        li.pop()
        if cur.rchild: # 要判断左右孩子是否存在，否则数组里会有None
            li.append(cur.rchild) 
        if cur.lchild:
            li.append(cur.lchild) 

def in_order(root): # 中序遍历
    if root: # 判断 root 是否存在
        in_order(root.lchild)
        print(root.data, end='')
        in_order(root.rchild)

def post_order(root): # 后序遍历
    if root: # 判断 root 是否存在
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end='')


from collections import deque
def level_order(root): # 层次遍历
    queue = deque()
    queue.append(root)
    print(root.data, end='')
    while queue: # queue 非空的前提下遍历
        node = queue.popleft() # 将队首元素记录，然后抛出队列
        if node.lchild:
            print(node.lchild.data, end='')
            queue.append(node.lchild)
        if node.rchild:
            print(node.rchild.data, end='')
            queue.append(node.rchild)
            
# level_order(e)
pre_order(e)
pre_order_iter(e)
#in_order(e)
#post_order(e)