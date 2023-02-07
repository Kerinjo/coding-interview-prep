import math
# On input: [-2, 0, 1, 2], target = 2
# return closest sum to the target -> [-2, 1, 2] (sum: 1)

def find_triplet(arr, target):
    arr.sort()
    difference = math.inf

    for i in range(len(arr)-2):
        left = i + 1  # since 'i' is covered
        right = len(arr) - 1
        while (left < right):
            target_diff = target - arr[i] - arr[left] - arr[right]
            if target_diff == 0:
                return target
            
            if abs(target_diff) < abs(difference) or \
                    abs(target_diff) == abs(difference) and \
                        target_diff > difference:
                difference = target_diff
            
            if target_diff > 0:  # move pointers according to difference value
                left += 1
            else:
                right -= 1
    return target - difference
            
