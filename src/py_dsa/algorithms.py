def linear_search(a, n, k):
    for i in range(n):
        if a[i] == k:
            return True
    return False