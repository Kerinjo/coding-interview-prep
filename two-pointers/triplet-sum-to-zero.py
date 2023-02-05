# Given an array of unsorted numbers,
# find all unique triplets in it that add up to zero.

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

def search_triplets(arr):
    # sort the array first
    arr.sort()
    triplets = []
    # X + Y + Z = 0  ==> Y + Z = -X
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)
    return triplets
    

def search_pair(arr, target_sum, start_pointer, triplets):
    end_pointer = len(arr) - 1
    while (start_pointer < end_pointer):
        pointer_sum = arr[start_pointer] + arr[end_pointer]
        if pointer_sum == target_sum:
            triplets.append([-target_sum, arr[start_pointer], arr[end_pointer]])
            start_pointer += 1
            end_pointer -= 1
            while start_pointer < end_pointer and arr[start_pointer] == arr[start_pointer - 1]:
                start_pointer += 1
            while start_pointer < end_pointer and arr[end_pointer] == arr[end_pointer + 1]:
                end_pointer -= 1
        elif target_sum > pointer_sum:
            start_pointer += 1
        else:
            end_pointer -= 1
