from triplet_sum_close_to_target import find_triplet
from triplets_with_smaller_sum import solution

assert find_triplet([-2, 0, 1, 2], 2) == 1
assert find_triplet([-3, -1, 1, 2], 1) == 0
assert find_triplet([1, 0, 1, 1], 100) == 3
assert find_triplet([0, 0, 1, 1, 2, 6], 5) == 4

assert solution([-1, 0, 2, 3], 3) == 2
assert solution([-1, 4, 2, 1, 3], 5) == 4

print("All tests went through.")

