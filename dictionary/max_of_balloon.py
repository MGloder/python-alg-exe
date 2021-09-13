class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res_dic = {}
        res_dic['b'] = 0
        res_dic['a'] = 0
        res_dic['l'] = 0
        res_dic['o'] = 0
        res_dic['n'] = 0
        for c in text:
            if c in res_dic:
                res_dic[c] += 1

        return int(min(min(min(min(res_dic['b'], res_dic['a']), res_dic['n']), res_dic['l'] / 2), res_dic['o'] / 2))
