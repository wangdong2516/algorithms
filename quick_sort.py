"""
    快速排序
        快速排序思路:
            1. 取一个元素p，使得元素p归位
            2. 列表被p分为两部分，左边的都比p小，右边的都比p大
            3. 递归完成排序
    快速排序的时间复杂度:Q(nlogn)
"""

from typing import List


def partiton(li: List, left: int, right:int) -> int :
    
    # 先拿一个变量将第一个元素的位置保存起来,这样左边就有空位了
    tmp = li[left]
    
    # left=right的时候，找到了这个位置
    while left < right:
        # 先从右边开始找,如果右边的值大于等于tmp，接着往前找
        while left < right and li[right] >= tmp:
            right -= 1

        # 当遇到右边的值比tmp小，将右边的值移动到空位上
        li[left] = li[right]
        print(li)

        # 从左边开始找，如果左边的值小于等于tmp，接着往后找
        while left < right and li[left] <= tmp:
            left += 1

        # 当遇到左边的值比tmp大，将左边的值移动到空位上
        li[right] = li[left]
        print(li)
    # 遍历完成，左边和右边指针重合，将tmp归位
    li[left] = tmp

    # 返回tmp所在的位置
    return left

def quick_sort(li: List, left: int, right: int) -> None:
    """
        快速排序
    """
    
    # 如果起始位置小于终止位置,说明列表的区域至少有两个元素，递归的终止条件
    if left < right:
        # 归位元素的位置
        mid = partiton(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 2, 3, 1, 9, 8, 6, 4, 7]
print(f'原数组:{li}')
quick_sort(li, 0, len(li) - 1)
print(li)


