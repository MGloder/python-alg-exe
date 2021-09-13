class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def format_output(start, end):
            if start == end:
                return f"{start}"
            return f"{start}->{end}"

        if len(nums) == 0:
            return []

        last_start = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                continue
            else:
                res.append(format_output(last_start, nums[i - 1]))
                last_start = nums[i]

        res.append(format_output(last_start, nums[len(nums) - 1]))

        return res
