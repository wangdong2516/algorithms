"""
    插入排序:
        插入排序的思想:

    时间复杂度:O(n2)
"""

from typing import List


def insert_sort(li):
    """
        插入排序
    """
    # 摸到的牌的位置
    for i in range(1, len(li)):
        
        # 手里最后一张牌的下标
        j = i - 1
        
        # 摸到的牌
        tmp = li[i]

        # 当摸到的牌比手里的最后一张牌小的时候并且手里的最后一张牌的下标是大于0的
        while tmp < li[j] and j >= 0:
            # 将手里的牌向后挪一位
            li[j + 1] = li[j]
            j -= 1
        
        # 将牌放到指定的位置
        li[j + 1] = tmp
        print(li)


li = [2, 1, 5, 9, 7, 3, 6, 4, 8]
insert_sort(li)
print(li)
