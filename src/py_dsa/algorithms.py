def linear_search(a, k):
    """
    Returns an integer

    Index is returned, if the key element is found in the list. Otherwise, -1 is returned.
    """
    for i in range(len(a)):
        if a[i] == k:
            return i
    return -1


def binary_search(a, k):
    """
    Returns an integer

    Index is returned, if the key element is found in the list. Otherwise, -1 is returned.
    """
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


def bubble_sort(a):
    """
    Returns None

    Internally sorts the given list by using the bubble sort algorithm - repeatedly swapping the adjacent elements if they are in unsorted order
    """
    n = len(a)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if a[j] >= a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


def insertion_sort(a):
    """
    Returns None

    Internally sorts the given list by using the insertion sort algorithm - list is virtually split into sorted and unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part. 
    """
    n = len(a)
    for i in range(1, n):
        temp = a[i]
        j = i - 1
        while(j >= 0 and temp < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
