def solution(nums):
    map_dict = {}
    for elem in nums:
        if elem in map_dict.keys():
            map_dict[elem] += 1
        else:
            map_dict[elem] = 1

    for key in map_dict.keys():
        if map_dict[key] > len(nums) / 2:
            return key


nums = [1,1,1,2,2,2,2,2]
print(solution(nums))
