class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = ""
        neg = False
        if num < 0:
            neg = True
            num = -num

        while num > 0:
            mod = num % 7
            res = str(mod) + res
            num = int(num / 7)

        if neg:
            return "-" + res
        return res