# Given a sorted array, create a new array containing squares
# of all the numbers of the input array in the sorted order.

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

def solution(arr):
    squares = [0 for x in range(len(arr))]
    left, right = 0, len(arr) - 1
    highest_square_index = len(arr) - 1
    while left <= right:
        left_square = arr[left]**2
        right_square = arr[right]**2
        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1
        highest_square_index -= 1
    return squares
