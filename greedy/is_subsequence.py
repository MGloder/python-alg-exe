class IsSubSequence:
    def __init__(self):
        """
         * Is Subsequence
         *
         * - Given a string s and a string t, check if s is subsequence of t.
         *
         * - Assumptions:
         *   1. There is only lower case English letters in both s and t.
         *   2. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
         *
         * - Follow up:
         *   If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to
         *   see if T has its subsequence. In this scenario, how would you change your code?
        """
        pass

    def is_subsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        while True:
            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
            else:
                t_index += 1

            if s_index == len(s):
                return True

            if t_index == len(t):
                return False
        return False

    def is_subsequence_dp(self, s, t):
        array = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for s_i in range(0, len(s)):
            for t_i in range(s_i, len(t)):
                current = 1 if t[t_i] == s[s_i] and s_i < t_i else 0
                array[s_i + 1][t_i + 1] = current + max(max(array[s_i][t_i], array[s_i][t_i + 1]), array[s_i + 1][t_i])
        return array[len(s)][len(t)] == len(s)

    def run(self):
        ## two pointer
        print(f"{self.is_subsequence('abc', 'ahbgdc')}")
        ## dp
        print(f"{self.is_subsequence_dp('bb', 'abcd')}")


if __name__ == '__main__':
    o = IsSubSequence()
    o.run()
