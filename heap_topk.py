"""
    topk问题

    现在有n个数，设计算法得到前k大的数

    解决思路:
       1. 排序后切片
       2. 冒泡、插入、选择排序
       3. 堆排序的思路:
            取列表前k个元素建立一个小根堆，堆顶就是目前第k大的数
            依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素，如果大于堆顶，则将堆顶更换为该元素，并且对堆进行一次调整。
            遍历列表所有元素之后，倒序弹出堆顶
"""

from typing import List


def sift(li: List, low: int, high: int):
    """
        调整函数
    """

    # 堆顶的位置
    i = low

    # 左孩子节点的位置
    j = 2 * i + 1

    # 堆顶元素
    tmp = li[low]

    # 当j没有越界的时候
    while j <= high:

        # 判断左孩子节点和右孩子节点谁大
        if j + 1 <= high and li[j+1] < li[j]:
            j = j + 1

        # 判断孩子节点和堆顶元素谁大
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1

        else:
            break

    li[i] = tmp


def topk(li: List, k: int) -> None:
    """
        topk问题
            时间复杂度:O(mlogn)
    """
    heap = li[0:k]
    for i in range((k-2) // 2, -1, -1):
        sift(heap, i, k-1)

    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)

    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)

    return heap


li = [1, 4, 3, 7, 8, 5, 6, 2, 9]

print(topk(li, 3))



