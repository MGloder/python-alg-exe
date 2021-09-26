class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nlogn
        sorted_nums = sorted(nums)

        # n
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                dic[num].append(index)
            else:
                dic[num] = [index]


        start_index = 0
        end_index = len(nums) - 1

        # n
        while True:
            rest = target - sorted_nums[start_index]
            while True:
                if sorted_nums[end_index] == rest:
                    if sorted_nums[start_index] ==  sorted_nums[end_index]:
                        return dic[sorted_nums[start_index]]
                    return [dic[sorted_nums[start_index]][0], dic[sorted_nums[end_index]][0]]
                elif sorted_nums[end_index] > rest:
                    end_index -= 1
                else:
                    break
            end_index = len(nums) - 1
            start_index += 1

        return null