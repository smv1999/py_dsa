## py-dsa

![GitHub followers](https://img.shields.io/github/followers/smv1999?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/smv1999/py_dsa?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/smv1999/py_dsa?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/smv1999/py_dsa?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/smv1999/py_dsa?color=blue&style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/py_dsa?color=blue&style=for-the-badge)

### Introduction 

The py-dsa module contains all the data structures and algorithms implementations.  

### Installation 

You can install the module using pip as shown below.

```bash
pip install py-dsa
```
### Usage

Consider the following examples :

```python
from py_dsa.data_structures import *

test_linkedlist = LinkedList()
test_linkedlist.add_first(10)
test_linkedlist.add_first(20)
test_linkedlist.add_first(30)
test_linkedlist.remove_last()
test_linkedlist.reverse_list()
test_linkedlist.print_list()
"""
Output :
20
30
"""
```

```python
from py_dsa.data_structures import *

test_tree = Tree()
test_tree.add(10)
test_tree.add(5)
test_tree.add(30)
print(test_tree.height())
test_tree.invert_tree()
test_tree.print_tree(traversal='postorder')
"""
Output:
2
30
5
10
"""
```

```python
from py_dsa.algorithms import *

a = [1, 2, 3, 4.5]
s = Searching()
print(s.linear_search(a, 3))
"""
Output : 
2
"""
```
### Testing 

To install py-dsa, along with the tools you need to develop and run tests. Run the following command :
```bash
$ pip install -e .[dev]
```

For running the tests, type the following command :

```bash
py.test
```

### Bugs/Requests 

Please use the [GitHub issue tracker](https://github.com/smv1999/py_dsa/issues) to submit bugs or request features.

### License 

Copyright Vaidhyanathan S M, 2021

Distributed under the terms of the [MIT](https://github.com/smv1999/py_dsa/blob/main/LICENSE) license, py-dsa is free and open source software.


