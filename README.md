# Unrolled Linked List

This repository contains starter code for lab 1 of BYU's CS498r: Problem Solving and Competitive Programming class


## What is an Unrolled Linked List?

An [Unrolled Linked List](https://en.wikipedia.org/wiki/Unrolled_linked_list) is essentially a Linked List, where each node contains a list of elements up to a given max node capacity

![alt text](https://upload.wikimedia.org/wikipedia/commons/1/16/Unrolled_linked_lists_%281-8%29.PNG)

### Pros

* Linked Lists are O(n) access. Having nodes that hold muliple elements in a list / array lowers that cost
* This also helps to lower the amount of memory used in a traditional Linked List

## Lab 1 Specs

### Requirements

### Grading

| Passes Unit Tests | 70 |
| Code Quality      | 15 |
| Test Coverage     | 15 |

## Code Quality

[PEP 8](https://www.python.org/dev/peps/pep-0008/) is a standard for writing clean and pythonic code. Although not all Python developers choose to follow it as a style guide, it is well accepted in the Python community. Feel free to approach the code quality portion of this assignment as you wish. You are not required to use PEP 8, but it is a really good option.

## unittest

unittest is a built-in testing framework for Python ([Python2](https://docs.python.org/2/library/unittest.html) or [Python2](https://docs.python.org/3/library/unittest.html)). There is some example code for you to get started in test_unrolled_linked_list.py

## Dunder Methods

Dunder stands for double underscores. Dunder methods are also refered to as magic methods, but don't use that term. They really aren't that magical.

Classes can implement dunder functions as needed. They allow operators and certain built-in python functions to work on the class. For example: adding two lists using the __add__ dunder function:

```python
l1 = [1,2,3,4]
l2 = [5,6,7,8]

l = l1 + l2
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8]
```




