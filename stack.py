class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        self.stack.pop()
        
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.stack) == 0 

def brace_match(s): # 括号匹配
    stack = Stack()
    match_dict = {')' : '(', ']' : '[', '}' : '{'} # 左右括号一一对应
    for brace in s:
        if brace in ['(', '[', '{']: # 判断元素是否属于左括号
            stack.push(brace)
        else:
            if stack.is_empty(): # 取出一个右括号后stack是否为空，为空则不匹配
                return 'Not match'
            elif stack.get_top() == match_dict[brace]: # 取出一个右括号后与stack最后一个元素进行匹配
                stack.pop() # 匹配成功！栈弹出数据
            else:
                return 'Not match' # 匹配不成功，判断不匹配
    if stack.is_empty(): # 遍历完之后判断stack是否为空，为空则所有括号匹配成功
        return 'Match'
    else: # 不为空则判断不匹配
        return 'Not match'
    
    
instance1 = '[([]{})(){[]}{()}]'
instance2 = '[{]'
print(brace_match(instance1))
print(brace_match(instance2))