class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(nums):
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
                            return nums
                    return nums

        orig = list(num)
        nums = list(num)
        for num_of_run in range(0, k):
            nums = next_permutation(nums)

        i = 0
        count = 0

        while i < len(nums):
            if nums[i] == orig[i]:
                i += 1
            else:
                j = i
                while nums[i] != orig[j]:
                    j += 1

                while j > i:
                    orig[j - 1], orig[j] = orig[j], orig[j - 1]
                    j -= 1
                    count += 1

        return count
