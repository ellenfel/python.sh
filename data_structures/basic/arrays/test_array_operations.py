import pytest
from array_operations import ArrayOperations

def test_find_max():
    assert ArrayOperations.find_max([1, 2, 3, 4, 5]) == 5
    assert ArrayOperations.find_max([-1, -2, -3, -4, -5]) == -1
    assert ArrayOperations.find_max([5]) == 5
    assert ArrayOperations.find_max([]) is None

def test_find_min():
    assert ArrayOperations.find_min([1, 2, 3, 4, 5]) == 1
    assert ArrayOperations.find_min([-1, -2, -3, -4, -5]) == -5
    assert ArrayOperations.find_min([5]) == 5
    assert ArrayOperations.find_min([]) is None

def test_reverse_array():
    assert ArrayOperations.reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert ArrayOperations.reverse_array([1]) == [1]
    assert ArrayOperations.reverse_array([]) == []

def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    assert ArrayOperations.binary_search(arr, 3) == 2
    assert ArrayOperations.binary_search(arr, 1) == 0
    assert ArrayOperations.binary_search(arr, 5) == 4
    assert ArrayOperations.binary_search(arr, 6) == -1

def test_remove_duplicates():
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    new_length = ArrayOperations.remove_duplicates(arr)
    assert new_length == 5
    assert arr[:new_length] == [1, 2, 3, 4, 5]

def test_rotate_array():
    arr = [1, 2, 3, 4, 5]
    assert ArrayOperations.rotate_array(arr.copy(), 2) == [4, 5, 1, 2, 3]
    assert ArrayOperations.rotate_array(arr.copy(), 0) == [1, 2, 3, 4, 5]
    assert ArrayOperations.rotate_array(arr.copy(), 5) == [1, 2, 3, 4, 5] 