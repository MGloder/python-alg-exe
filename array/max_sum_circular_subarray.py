class Solution:
    def getMaxResult(self, start_index, nums: List[int], current_step) -> int:
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
            right = self.getMaxResult(central_index, completed_array, max_step)
            result = max(right, result)

        return result
