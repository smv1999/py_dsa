from py_dsa.algorithms import *

def test_py_dsa_algorithms_linear_search():
    assert linear_search([1,2,3,4,5], 4) == 3

def test_py_dsa_algorithms_binary_search():
    assert binary_search([1,2,3,4,5], 3) == 2