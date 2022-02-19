"""
    冒泡排序python实现
        冒泡排序思路:
            重复的遍历要排序的列表,一次比较两个元素,如果顺序不对就进行交换，知道没有需要交换的数据为止，整个列表就是有序的。
"""

from typing import List


def bubble_sort(li: List) -> List:

    """
        冒泡排序 升序版本
    """

    # 需要循环的次数，n-1次
    for i in range(len(li) - 1):
        # 每次循环需要做的事，就是比较相邻两个元素的大小，将最大的元素自动到最后

        # 简化步骤，判断每次循环中是否发生了元素交换，如果没有发生元素交换，就已经是有序的了，没有必要在进行遍历了
        exchange = False

        # 随着循环次数的增加，有序区的元素逐渐增加，无序区的元素逐渐减少
        for j in range(0, len(li) - i - 1):
            # 前面的元素比后面的元素大，交换两个元素的位置，将exchange=True
            # li[j] < li[j + 1],排出来的就是降序的
            if li[j] > li[j + 1]:
                li[j + 1], li[j] = li[j], li[j + 1]
                exchange = True

        # 如果在一次循环中没有发生元素交换，就认为整个列表已经有序
        if not exchange:
            break
        print(li)
    return li




li = [3, 5, 9, 2, 1, 6, 7, 4, 8]
print(bubble_sort(li))


