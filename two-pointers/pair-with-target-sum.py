# Given an array of sorted numbers and a target sum,
# find a pair in the array whose sum is equal to the given target.

def solution(arr, target_sum):
    start_pointer = 0
    end_pointer = len(arr) - 1

    pointer_sum = arr[start_pointer] + arr[end_pointer]
    
    while (pointer_sum != target_sum):
        if (pointer_sum > target_sum):
            end_pointer -= 1 
        
        if (pointer_sum < target_sum):
            start_pointer += 1
        
        pointer_sum = arr[start_pointer] + arr[end_pointer]

    return [start_pointer, end_pointer]
