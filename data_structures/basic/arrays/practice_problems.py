"""
Array Practice Problems

This file contains common array-related interview questions and their solutions.
Each problem includes:
1. Problem statement
2. Solution approach
3. Time and space complexity analysis
4. Implementation
"""

class ArrayPractice:
    @staticmethod
    def two_sum(nums, target):
        """
        Problem: Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        
        Approach: Use a hash map to store seen numbers and their indices.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

    @staticmethod
    def max_subarray(nums):
        """
        Problem: Find the contiguous subarray with the largest sum.
        
        Approach: Kadane's Algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    @staticmethod
    def move_zeros(nums):
        """
        Problem: Move all zeros to the end while maintaining the relative order
        of non-zero elements.
        
        Approach: Two-pointer technique
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        write_index = 0
        for num in nums:
            if num != 0:
                nums[write_index] = num
                write_index += 1
        
        while write_index < len(nums):
            nums[write_index] = 0
            write_index += 1
        return nums

    @staticmethod
    def contains_duplicate(nums):
        """
        Problem: Check if array contains any duplicates.
        
        Approach: Use a set to track seen numbers
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    @staticmethod
    def rotate_image(matrix):
        """
        Problem: Rotate a 2D matrix 90 degrees clockwise.
        
        Approach: Transpose and reverse each row
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for row in matrix:
            row.reverse()
        return matrix

# Example usage
if __name__ == "__main__":
    # Test cases
    print("Two Sum:")
    print(ArrayPractice.two_sum([2, 7, 11, 15], 9))  # [0, 1]
    
    print("\nMax Subarray:")
    print(ArrayPractice.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    
    print("\nMove Zeros:")
    print(ArrayPractice.move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
    
    print("\nContains Duplicate:")
    print(ArrayPractice.contains_duplicate([1, 2, 3, 1]))  # True
    
    print("\nRotate Image:")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(ArrayPractice.rotate_image(matrix))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]] 