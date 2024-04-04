def partition(li:list, left:int, right:int):
    '''
    输入 li, left, right
    输出 将li[left]在li中的正确位置
    '''
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: # 从右向左查找小于tmp的数
            right -= 1 # 向左移动
        li[left] = li[right] # 将小于tmp的数放到左侧
        # print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
        # print(li, 'left')
    li[left] = tmp
    return left
    
# li = [5,7,4,6,3,1,2,9,8]
# print(li)
# partition(li, 0, len(li)-1)
# print(li)
def quick_sort(li:list, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)
    return li

li = [5,7,4,6,3,1,2,9,8]
print(quick_sort(li, 0, len(li)-1))