"""
    基数排序:
        基数排序是一种借助“多关键字排序”的思想来实现“单关键字排序”的内部排序算法。

    多关键字排序:
        对多个关键字进行排序，每个记录的最终位置由多个关键字决定

    基数排序的时间复杂度:O(kn) --> 线性时间复杂度
    基数排序的空间复杂度:O(k + n)
    k表示数字的最大位数
"""


from typing import List


def radix_sort(li: List) -> None:
    """
        基数排序
    """

    # 确定最大值
    max_num = max(li)

    # 最大数的位数决定循环的次数
    it = 0
    
    # 确定循环的次数
    while 10 ** it <= max_num:
        
        # 分桶0-9
        buckets = [[] for _ in range(10)]
        
        for val in li:

            # 取对应位置上的数字 
            digit = (val // (10 ** it)) % 10

            buckets[digit].append(val)

        # 桶已经分完了
        li.clear()
        
        # 把数重新写回li
        for bucket in buckets:
            for var in bucket:
                li.append(var)

        it += 1

li = [3, 5, 1, 7, 4, 6, 9, 8, 2]
radix_sort(li)
print(li)
