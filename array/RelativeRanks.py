class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score)[::-1]
        dic = {}
        for i, s in enumerate(sorted_score):
            if i == 0:
                dic[s] = 'Gold Medal'
            elif i == 1:
                dic[s] = 'Silver Medal'
            elif i == 2:
                dic[s] = 'Bronze Medal'
            else:
                dic[s] = str(i + 1)


        get_res = lambda x: dic[x]

        return list(map(get_res, [x for x in score]))