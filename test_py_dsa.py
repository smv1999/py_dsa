from py_dsa.algorithms import *
from py_dsa.data_structures import *

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


def test_py_dsa_datastructures_stack():
    test_stack = Stack()
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(4)
    test_stack.push(5)
    assert test_stack.pop() == 5


def test_py_dsa_datastructures_queue():
    test_queue = Queue()
    test_queue.enqueue(1)
    test_queue.enqueue(2)
    test_queue.enqueue(3)
    test_queue.enqueue(4)
    test_queue.enqueue(5)
    assert test_queue.dequeue() == 1


def test_py_dsa_datastructures_linkedlist():
    test_linkedlist = LinkedList()
    test_linkedlist.add_first(10)
    test_linkedlist.add_first(20)
    test_linkedlist.add_first(30)
    assert test_linkedlist.head.data == 30
