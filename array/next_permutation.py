class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 1:
            return nums

        for index_from_back in range(len(nums) - 1, 0, -1):
            if nums[index_from_back - 1] < nums[index_from_back]:
                to_be_replaced = nums[index_from_back - 1]
                for i1 in range(index_from_back, len(nums)):
                    for i2 in range(i1 + 1, len(nums)):
                        if nums[i1] > nums[i2]:
                            temp = nums[i2]
                            nums[i2] = nums[i1]
                            nums[i1] = temp

                for index in range(index_from_back, len(nums)):
                    if to_be_replaced < nums[index]:
                        temp = nums[index]
                        nums[index] = nums[index_from_back - 1]
                        nums[index_from_back - 1] = temp
                        return
                return

        for index in range(0, int(len(nums) / 2)):
            temp = nums[index]
            nums[index] = nums[len(nums) - index - 1]
            nums[len(nums) - index - 1] = temp
        return
