def linear_search(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1


def binary_search(a, k):
    first = 0
    last = len(a) - 1
    while first <= last:
        mid = (first + last) // 2
        if a[mid] == k:
            return mid
        elif a[mid] < k:
            first = mid + 1
        elif a[mid] > k:
            last = mid - 1
    return -1
