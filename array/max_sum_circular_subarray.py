class Solution:
    def getMaxResult(self, start_index, direction, nums: List[int], current_step) -> int:
        if direction < 0:
            if current_step > 1:
                if start_index > 0 and start_index <= len(nums) - 1:
                    return max(nums[start_index],
                               nums[start_index] +
                               self.getMaxResult(start_index - 1, -1, nums, current_step - 1))
                else:
                    return nums[start_index]
            else:
                return nums[start_index]
        else:
            if current_step > 1:
                if start_index >= 0 and start_index < len(nums) - 1:
                    return max(nums[start_index],
                               nums[start_index] +
                               self.getMaxResult(start_index + 1, 1, nums, current_step - 1))
                else:
                    return nums[start_index]
            else:
                return nums[start_index]

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)

        completed_array = nums + nums[:len(nums) - 1]
        max_step = len(nums)
        result = float('-inf')

        for central_index in range(0, len(completed_array)):
            left = self.getMaxResult(central_index, -1, completed_array, max_step)
            right = self.getMaxResult(central_index, 1, completed_array, max_step)
            result = max(max(left, right), result)

        return result
