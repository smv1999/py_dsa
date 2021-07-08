from py_dsa.algorithms import *

search_arr = Searching()
sort_arr = Sorting()


def test_py_dsa_algorithms_linear_search():
    assert search_arr.linear_search([1, 2, 3, 4, 5], 4) == 3


def test_py_dsa_algorithms_binary_search():
    assert search_arr.binary_search([1, 2, 3, 4, 5], 3) == 2


def test_py_dsa_algorithms_jump_search():
    assert search_arr.jump_search([1, 2, 3, 4, 5], 5) == 4


def test_py_dsa_algorithms_bubble_sort():
    test_arr = [3, 1, 5, 4, 2]
    sort_arr.bubble_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]


def test_py_dsa_algorithms_insertion_sort():
    test_arr = [3, 1, 5, 4, 2]
    sort_arr.insertion_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]


def test_py_dsa_algorithms_selection_sort():
    test_arr = [3, 1, 5, 4, 2]
    sort_arr.selection_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]


def test_py_dsa_algorithms_quick_sort():
    test_arr = [3, 1, 5, 4, 2]
    sort_arr.quick_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]


def test_py_dsa_algorithms_merge_sort():
    test_arr = [3, 1, 5, 4, 2]
    sort_arr.merge_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]


def test_py_dsa_algorithms_heap_sort():
    test_arr = [3, 1, 5, 4, 2]
    sort_arr.heap_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]


def test_py_dsa_algorithms_radix_sort():
    test_arr = [3, 1, 5, 4, 2]
    sort_arr.radix_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]


def test_py_dsa_algorithms_shell_sort():
    test_arr = [3, 1, 5, 4, 2]
    sort_arr.shell_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]
