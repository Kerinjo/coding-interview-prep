# Given an array of sorted numbers, remove all duplicate number instances
# from it in-place, such that each element appears only once.
# The relative order of the elements should be kept the same
# and you should _not use any extra space_. Space complexity of O(1).
# Return the length of the subarray that has no duplicates in it.

def solution(arr):

    i = 0
    next_non_duplicate = 1

    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate
