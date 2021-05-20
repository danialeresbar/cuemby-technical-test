def canBeSplitted(array):
    """

    :param array: array of elements to which the check will be applied
    :return: Integer which indicates if the array can be split
    """

    if not array:
        return 0

    for index, _ in enumerate(array):
        if index > 0:
            left_slice = array[:index]
            right_slice = array[index:]
            if sum(left_slice) == sum(right_slice):
                return 1

    return -1


if __name__ == '__main__':
    matrix = [1, 3, 3, 8, 4, 3, 2, 3, 3]
    print(canBeSplitted(matrix))
