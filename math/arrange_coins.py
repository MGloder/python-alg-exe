class Solution:
    """
    https://leetcode.com/problems/arranging-coins/submissions/
    """
    def arrangeCoins(self, n: int) -> int:
        x = 0
        current_sum = 0
        while True:
            if n >= current_sum:
                x += 1
                current_sum += x
            else:
                break

        return x - 1