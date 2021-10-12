class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + int((end - start) / 2)
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid
            elif nums[mid] == target:
                return mid

            if start == end and nums[start] != target:
                return -1
            if abs(start - end) == 1:
                if nums[start] == target:
                    return start
                if nums[end] == target:
                    return end
                return - 1
        return -1
