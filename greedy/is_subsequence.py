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

    def run(self):
        pass


if __name__ == '__main__':
    o = IsSubSequence()
    o.run()
