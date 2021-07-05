from py_dsa.algorithms import *

test_arr = [3, 1, 5, 4, 2]


def test_py_dsa_algorithms_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 4) == 3


def test_py_dsa_algorithms_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2


def test_py_dsa_algorithms_bubble_sort():
    bubble_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]


def test_py_dsa_algorithms_insertion_sort():
    insertion_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5]
