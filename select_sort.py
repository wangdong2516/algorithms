"""
    选择排序
        选择排序的思想:
            每次循环选择一个最大或者最小的数，放到有序区。
"""
from typing import List


def select_sort(li: List) -> None:
    """
        选择排序
    """
    
    # 循环的次数，n-1次
    for i in range(len(li) - 1):
        # 最小元素的下标，假设第一个元素就是最小的
        min_loc = i
        # 每次选出一个最小的数
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                # 将min_loc指向新的位置
                min_loc = j

        # 遍历一次，找到了最小的元素，进行交换
        li[i], li[min_loc] = li[min_loc], li[i]


a = [3, 5, 1, 8, 9, 2, 4, 7, 6]
select_sort(a)
print(a)
