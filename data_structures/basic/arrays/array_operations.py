"""
Array Operations and Implementations

This module provides implementations of common array operations and algorithms.
"""

class ArrayOperations:
    @staticmethod
    def find_max(arr):
        """Find the maximum element in an array."""
        if not arr:
            return None
        max_val = arr[0]
        for num in arr[1:]:
            if num > max_val:
                max_val = num
        return max_val

    @staticmethod
    def find_min(arr):
        """Find the minimum element in an array."""
        if not arr:
            return None
        min_val = arr[0]
        for num in arr[1:]:
            if num < min_val:
                min_val = num
        return min_val

    @staticmethod
    def reverse_array(arr):
        """Reverse the elements of an array in-place."""
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    @staticmethod
    def binary_search(arr, target):
        """Perform binary search on a sorted array."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @staticmethod
    def remove_duplicates(arr):
        """Remove duplicates from a sorted array in-place."""
        if not arr:
            return 0
        write_index = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[write_index] = arr[i]
                write_index += 1
        return write_index

    @staticmethod
    def rotate_array(arr, k):
        """Rotate array to the right by k steps."""
        n = len(arr)
        k = k % n
        arr[:] = arr[-k:] + arr[:-k]
        return arr

# Example usage
if __name__ == "__main__":
    # Test cases
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    print("Max value:", ArrayOperations.find_max(arr))
    print("Min value:", ArrayOperations.find_min(arr))
    print("Reversed array:", ArrayOperations.reverse_array(arr.copy()))
    print("Binary search for 3:", ArrayOperations.binary_search(sorted(arr), 3))
    
    arr_with_duplicates = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    print("\nArray with duplicates:", arr_with_duplicates)
    new_length = ArrayOperations.remove_duplicates(arr_with_duplicates)
    print("After removing duplicates:", arr_with_duplicates[:new_length])
    
    print("\nRotate array by 2 positions:", ArrayOperations.rotate_array(arr.copy(), 2)) 