import pytest
from practice_problems import ArrayPractice

def test_two_sum():
    assert ArrayPractice.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert ArrayPractice.two_sum([3, 2, 4], 6) == [1, 2]
    assert ArrayPractice.two_sum([3, 3], 6) == [0, 1]
    assert ArrayPractice.two_sum([1, 2, 3], 7) == []

def test_max_subarray():
    assert ArrayPractice.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert ArrayPractice.max_subarray([1]) == 1
    assert ArrayPractice.max_subarray([5, 4, -1, 7, 8]) == 23
    assert ArrayPractice.max_subarray([-1, -2, -3]) == -1
    assert ArrayPractice.max_subarray([]) == 0

def test_move_zeros():
    assert ArrayPractice.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert ArrayPractice.move_zeros([0]) == [0]
    assert ArrayPractice.move_zeros([1, 0, 0, 0, 0]) == [1, 0, 0, 0, 0]
    assert ArrayPractice.move_zeros([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_contains_duplicate():
    assert ArrayPractice.contains_duplicate([1, 2, 3, 1]) is True
    assert ArrayPractice.contains_duplicate([1, 2, 3, 4]) is False
    assert ArrayPractice.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert ArrayPractice.contains_duplicate([1]) is False

def test_rotate_image():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected1 = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    assert ArrayPractice.rotate_image(matrix1) == expected1

    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    expected2 = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
    assert ArrayPractice.rotate_image(matrix2) == expected2 