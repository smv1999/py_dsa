class Searching:
    def linear_search(self, a, k):
        """
        Returns an integer

        Index is returned, if the key element is found in the list. Otherwise, -1 is returned.
        """
        for i in range(len(a)):
            if a[i] == k:
                return i
        return -1

    def binary_search(self, a, k):
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

    def jump_search(self, a, k):
        """
        Returns an integer

        Index is returned, if the key element is found in the list. Otherwise, -1 is returned.
        """
        step = 0
        while a[step] < k:
            step += 1
        i = step
        while i < len(a):
            if a[i] == k:
                return i
            i += step
        return -1


class Sorting:
    def bubble_sort(self, a):
        """
        Returns None

        Internally sorts the given list by using the bubble sort algorithm - repeatedly swapping the adjacent elements if they are in unsorted order
        """
        n = len(a)
        for i in range(n-1):
            for j in range(0, n - i - 1):
                if a[j] >= a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]

    def insertion_sort(self, a):
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

    def selection_sort(self, a):
        """
        Returns None

        Internally sorts the given list by using the selection sort algorithm - repeatedly picking the smallest element from the unsorted part and placing it at the correct position in the sorted part.
        """
        n = len(a)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if a[j] < a[min_index]:
                    min_index = j
            if min_index != i:
                a[i], a[min_index] = a[min_index], a[i]

    def quick_sort(self, a):
        """
        Returns None

        Internally sorts the given list by using the quick sort algorithm - the list is split into two parts. The left part is sorted, the right part is sorted recursively.
        """
        n = len(a)
        self.__quick_sort_helper(a, 0, n-1)

    def __quick_sort_helper(self, a, low, high):
        if low < high:
            pivot = self.__partition(a, low, high)
            self.__quick_sort_helper(a, low, pivot-1)
            self.__quick_sort_helper(a, pivot+1, high)

    def __partition(self, a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[high] = a[high], a[i+1]
        return i+1

    def merge_sort(self, a):
        """
        Returns None

        Internally sorts the given list by using the merge sort algorithm - the list is split into two parts. The left part is sorted, the right part is sorted recursively.
        """
        if len(a) > 1:

            mid = len(a)//2

            L = a[:mid]

            R = a[mid:]

            self.merge_sort(L)

            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    a[k] = L[i]
                    i += 1
                else:
                    a[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                a[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                a[k] = R[j]
                j += 1
                k += 1

    def heap_sort(self, a):
        """
        Returns None

        Internally sorts the given list by using the heap sort algorithm - the list is first converted into a heap. Then, the heap is repeatedly reduced to a sorted list.
        """
        n = len(a)

        for i in range(n//2 - 1, -1, -1):
            self.__heapify(a, n, i)

        for i in range(n-1, 0, -1):
            a[i], a[0] = a[0], a[i]
            self.__heapify(a, i, 0)

    def __heapify(self, a, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.__heapify(a, n, largest)

    def radix_sort(self, a):
        """
        Returns None

        Internally sorts the given list by using the radix sort algorithm - the list is first converted into a list of digits. Then, the list is repeatedly sorted by the digits.
        """
        max1 = max(a)

        exp = 1
        while max1 / exp > 0:
            self.__counting_sort(a, exp)
            exp *= 10

    def __counting_sort(self, a, exp):
        n = len(a)
        b = [0] * n
        count = [0] * 10
        for i in range(0, n):
            index = (a[i] // exp)
            count[(index) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(n-1, -1, -1):
            index = (a[i] // exp)
            b[count[(index) % 10] - 1] = a[i]
            count[(index) % 10] -= 1
        for i in range(0, n):
            a[i] = b[i]

    def shell_sort(self, a):
        """
        Returns None

        Internally sorts the given list by using the shell sort algorithm - the list is first converted into a list of sublists. Then, the list is repeatedly sorted by the sublists.
        """
        n = len(a)
        h = 1
        while h < n//3:
            h = 3*h + 1
        while h >= 1:
            for i in range(h, n):
                for j in range(i, h-1, -h):
                    if a[j] < a[j-h]:
                        a[j], a[j-h] = a[j-h], a[j]
            h = h//3
