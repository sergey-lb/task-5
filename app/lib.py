def is_sorted_list(data):
    """
    >>> is_sorted_list([1,2,3])
    True

    >>> is_sorted_list([3,2,1])
    True

    >>> is_sorted_list([2,1,3])
    False
    """
    copy = data[:]

    copy.sort()
    if data == copy:
        return True

    copy.sort(reverse=True)
    if data == copy:
        return True

    return False
