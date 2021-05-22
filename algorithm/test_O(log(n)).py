def canBeSplitted(array):
    """
    O(n) complexity by applying the Dynamic programming technique
    :param array: array of elements to which the check will be applied
    :return: Integer which indicates if the array can be split
    """

    if not array:
        return 0

    target = sum(array) / 2
    min_index = 0
    max_index = len(array) - 1

    while True:
        pivot = (max_index + min_index) // 2
        left_sum = sum(array[0:pivot + 1])

        if left_sum == target:
            return 1
        elif pivot == min_index or pivot == max_index:
            break
        elif left_sum < target:
            min_index = pivot
        elif left_sum > target:
            max_index = pivot

    return -1


if __name__ == '__main__':
    tests = [
        [1, 3, 3, 8, 4, 3, 2, 3, 3],
        [],
        [1, 2, 3],
        [1, 2, 3, 2],
        [4],
        [1, 2, 3, 5, 1],
        [27, 1, 2, 3, 4, 5, 6, 6],
        [1, 2, 3, 4, 5, 6, 6, 27],
        [9, 9, 19, 14, 7, 9, 1, 7, 5, 14, 2, 18, 7, 5, 15, 14, 4, 3, 14, 16, 3, 6, 1, 12, 5, 16, 1, 2, 18, 11, 3, 10, 2,
         1, 10, 11, 16, 1, 12, 19, 4, 19, 15, 13, 16, 12, 3, 18, 19, 16, 5, 9, 18, 7, 3, 17, 17, 7, 19, 17, 7, 12, 18,
         4, 1, 17, 4, 15, 16, 13, 10, 6, 5, 15, 11, 4, 4, 7, 11, 10, 12, 11, 3, 15, 14, 6, 19, 12, 7, 6, 11, 11, 1, 16,
         12, 11, 16, 18, 5, 6, 1008],
        [16, 18, 2, 5, 17, 19, 4, 4, 12, 5, 1, 9, 5, 11, 16, 17, 13, 8, 7, 19, 8, 16, 4, 19, 6, 17, 3, 10, 8, 19, 19, 9,
         1, 17, 6, 3, 7, 12, 7, 15, 2, 5, 4, 5, 17, 14, 19, 12, 19, 6, 15, 3, 16, 18, 13, 12, 12, 9, 7, 15, 7, 3, 11,
         15, 19, 12, 14, 13, 16, 15, 4, 1, 8, 16, 8, 5, 15, 11, 7, 14, 7, 13, 14, 17, 19, 13, 18, 17, 14, 15, 17, 12, 8,
         8, 1, 12, 12, 15, 16, 7, 19, 15, 13, 15, 5, 2, 6, 17, 14, 7, 18, 12, 4, 13, 2, 4, 4, 19, 1, 6, 16, 1, 10, 17,
         6, 14, 1, 6, 5, 11, 7, 11, 5, 12, 19, 5, 17, 9, 17, 7, 1, 8, 12, 2, 11, 1, 10, 6, 9, 12, 4, 12, 6, 11, 19, 16,
         15, 2, 10, 5, 8, 19, 16, 18, 1, 3, 8, 16, 18, 4, 9, 9, 4, 14, 8, 19, 6, 2, 12, 16, 4, 3, 2, 15, 11, 3, 5, 6, 2,
         15, 6, 12, 15, 6, 1, 9, 2, 16, 16, 12, 18, 11, 3, 19, 7, 7, 19, 14, 6, 14, 12, 11, 6, 2, 4, 5, 17, 3, 16, 12,
         1, 4, 5, 12, 15, 11, 3, 8, 9, 5, 11, 12, 4, 3, 9, 7, 3, 11, 12, 12, 3, 7, 15, 2, 15, 12, 19, 18, 3, 9, 11, 18,
         14, 11, 3, 11, 3, 10, 8, 11, 1, 12, 6, 3, 10, 4, 12, 10, 8, 2, 4, 12, 1, 6, 13, 2, 6, 6, 9, 4, 19, 18, 1, 13,
         9, 7, 8, 5, 16, 3, 2, 5, 1, 6, 11, 12, 9, 1, 1, 6, 13, 14, 15, 8, 15, 15, 11, 5, 19, 9, 13, 3, 1, 6, 10, 17, 5,
         4, 13, 3, 9, 19, 15, 7, 11, 12, 8, 13, 9, 10, 18, 16, 5, 4, 15, 15, 14, 18, 1, 13, 3, 3, 6, 2, 2, 18, 13, 13,
         16, 19, 10, 15, 7, 13, 10, 2, 10, 13, 9, 14, 15, 16, 2, 6, 13, 9, 6, 14, 16, 18, 7, 4, 6, 5, 8, 12, 9, 17, 17,
         17, 11, 8, 18, 10, 5, 14, 15, 15, 13, 2, 12, 8, 18, 18, 12, 1, 11, 19, 19, 4, 19, 13, 7, 9, 9, 1, 8, 5, 18, 9,
         1, 17, 10, 17, 7, 7, 5, 17, 7, 1, 19, 2, 9, 11, 12, 14, 13, 12, 5, 10, 9, 13, 12, 17, 2, 17, 10, 19, 1, 16, 4,
         19, 4, 8, 9, 8, 3, 19, 11, 19, 8, 19, 2, 15, 9, 2, 12, 8, 7, 1, 6, 7, 2, 14, 4, 13, 16, 4, 1, 16, 10, 15, 4, 6,
         15, 10, 2, 19, 5, 3, 18, 4, 18, 19, 14, 19, 14, 8, 7, 13, 8, 9, 16, 19, 4, 18, 3, 7, 11, 6, 8, 9, 7, 19, 17, 3,
         9, 13, 10, 12, 10, 2, 19, 14, 3, 17, 1, 18, 5, 10, 10, 4, 19, 13, 8, 16, 12, 5, 15, 17, 16, 9, 6, 6, 13, 18,
         12, 17, 4, 14, 8, 18, 1, 16, 8, 5, 16, 10, 11, 5, 2, 1, 4, 8, 13, 6, 17, 11, 17, 11, 12, 1, 16, 12, 3, 13, 14,
         14, 6, 2, 19, 12, 15, 7, 10, 10, 19, 18, 9, 1, 12, 1, 5, 16, 5, 3, 1, 3, 10, 12, 13, 4, 9, 8, 7, 2, 6, 15, 4,
         12, 17, 19, 1, 3, 17, 12, 19, 9, 2, 5, 5, 9, 15, 19, 6, 18, 3, 6, 6, 8, 19, 19, 12, 3, 10, 5, 4, 3, 17, 16, 2,
         5, 3, 15, 18, 13, 13, 16, 18, 3, 15, 3, 7, 19, 9, 9, 13, 15, 18, 14, 7, 2, 19, 11, 17, 12, 2, 9, 2, 14, 9, 11,
         14, 1, 11, 18, 13, 9, 18, 8, 12, 9, 9, 10, 4, 12, 7, 18, 2, 7, 15, 8, 11, 14, 3, 17, 5, 11, 11, 18, 19, 19, 12,
         13, 18, 2, 19, 19, 1, 4, 18, 6, 11, 6, 13, 8, 7, 2, 4, 6, 4, 5, 13, 13, 4, 2, 13, 7, 3, 14, 13, 7, 5, 14, 17,
         6, 11, 12, 15, 18, 2, 9, 1, 18, 4, 9, 3, 11, 8, 8, 17, 11, 19, 5, 12, 14, 2, 1, 6, 8, 2, 4, 11, 18, 13, 6, 12,
         15, 7, 7, 5, 6, 2, 11, 6, 9, 19, 8, 17, 6, 14, 12, 9, 16, 1, 7, 14, 5, 3, 1, 13, 14, 6, 15, 4, 7, 16, 8, 6, 9,
         5, 10, 7, 4, 1, 8, 9, 5, 12, 14, 4, 11, 1, 19, 16, 1, 18, 4, 11, 14, 12, 13, 12, 14, 4, 6, 5, 10, 7, 6, 3, 11,
         7, 15, 4, 12, 15, 4, 4, 10, 8, 11, 6, 5, 1, 12, 1, 19, 7, 3, 4, 11, 17, 12, 18, 12, 10, 13, 9, 9, 18, 13, 1, 8,
         9, 3, 11, 13, 18, 6, 18, 7, 7, 19, 7, 19, 15, 8, 7, 1, 14, 16, 19, 10, 17, 15, 1, 11, 10, 6, 4, 16, 15, 19, 11,
         4, 5, 13, 18, 10, 13, 11, 3, 5, 8, 12, 15, 12, 2, 19, 8, 3, 10, 3, 18, 3, 19, 3, 16, 12, 15, 2, 5, 1, 8, 1, 11,
         11, 14, 11, 5, 12, 11, 13, 19, 9, 17, 16, 8, 14, 2, 16, 10, 16, 2, 2, 10, 5, 2, 1, 7, 11, 2, 17, 10, 8, 11, 14,
         17, 19, 14, 13, 13, 2, 7, 13, 6, 7, 6, 16, 4, 14, 1, 10, 17, 2, 8, 5, 10, 5, 7, 14, 19, 3, 9, 3, 17, 15, 14,
         15, 6, 14, 7, 9, 16, 6, 15, 19, 19, 16, 16, 18, 17, 8, 5, 4, 12, 7, 1, 9, 9914]
    ]

    for test in tests:
        print(canBeSplitted(test))
