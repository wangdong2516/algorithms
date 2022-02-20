"""
    计数排序
"""

from typing import List


def count_sort(li: List, max_num: int) -> List:
    """
        计数排序
    """

    count = [0 for i in range(max_num + 1)]
    res = list()

    for val in li:
        count[val] += 1
    
    for index, value in enumerate(count):
        for i in range(value):
            res.append(index)
    
    return res


a = [1, 5, 3, 4, 6, 7, 9, 8, 2]
print(count_sort(a, 9))


