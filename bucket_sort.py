"""
    桶排序:
        桶排序思路:
            首先将元素分在不同的桶中，再对每个桶中的元素进行排序

    桶排序的时间复杂度:
        桶排序的表现取决于数据的分布，也就是需要对不同数据排序时采用不同的分桶策略
        平均情况时间复杂度:O(n+k)
        最坏情况时间复杂度:O(n2k)
        空间复杂度:O(nk)
"""

from typing import List
import random


def bucket_sort(li: List, n:int=10, max_num:int=100):
    """
        桶排序

        n:分成多少个桶
        max_num:列表中最大的元素

    """
    
    # 创建桶列表
    buckets = [[] for _ in range(n)]
    
    for val in li:
        # 决定数放到哪个桶里
        index = min(val // (max_num // n), n - 1)
        
        # 将元素放到桶里
        buckets[index].append(val)
        
        # 插入完成之后对桶进行排序
        for j in range(len(buckets[index]) - 1, 0, -1):
            if buckets[index][j] < buckets[index][j - 1]:
                buckets[index][j], buckets[index][j - 1] = buckets[index][j - 1], buckets[index][j]
            else:
                break

    
    # 挨个出数
    res = []

    for bucket in buckets:
        for val in bucket:
            res.append(val)

    return res


li = [random.randint(0, 1000) for i in range(1000)]
li = bucket_sort(li)
print(li)


