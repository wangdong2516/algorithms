"""
    归并排序:
        归并排序使用的是分治的思想
        1. 将n个元素分成个含n/2个元素的子序列。
        2. 用合并排序法对两个子序列递归的排序。
        3. 合并两个已排序的子序列已得到排序结果。
    这种操作称为一次归并

    时间复杂度:O(nlogn)，这个是平均时间复杂度，最佳时间复杂度为O(n)
        
"""

from typing import List


def merge(li: List, low: int, mid:int, high: int) -> List:
    """
        合并
    """

    i = low

    j = mid + 1

    res = []

    # 确保左右两边都有数 
    while i <= mid and j <= high:
        
        if li[i] < li[j]:
            res.append(li[i])
            i += 1

        else:
            res.append(li[j])
            j += 1

    # 两边有任意一部分没数了
    while i <= mid:
        res.append(li[i])
        i += 1

    while j <= high:
        res.append(li[j])
        j += 1
    
    li[low: high + 1] = res

    return li


def merge_sort(li: List, low: int, high:int):
    """
        归并排序
        1. 分解:将列表越分越小，直至分为一个元素
        2. 终止条件:一个元素是有序的
        3. 将两个有序列表合并，列表越来越大
    """

    # 至少有两个元素
    if low < high:
        mid = (low + high) // 2
        # 分解左边
        merge_sort(li, low, mid)
        # 分解右边
        merge_sort(li, mid + 1, high)
        # 合并左边和右边
        merge(li, low, mid, high)


li = [2, 4, 5, 7, 1, 3, 6, 8, 9]
#merge(li, 0, 3, 8)
merge_sort(li, 0, 8)
print(li)

