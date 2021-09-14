class LicenseKeyFormatting:
    """
    You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
    The string is separated into n + 1 groups by n dashes. You are also given an integer k.

    We want to reformat the string s such that each group contains exactly k characters, except for the first group,
    which could be shorter than k but still must contain at least one character.
    Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

    Return the reformatted license key.
    """

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_str = s.replace("-", "").upper()
        res = []
        for i in range(len(new_str), 0, -k):
            if i - k < 0:
                break
            res = [f'{new_str[i - k:i]}'] + res

        if len(new_str) % k != 0:
            res = [f'{new_str[0:(len(new_str) % k)]}'] + res

        return '-'.join(res)

    def run(self):
        self.licenseKeyFormatting("5F3Z-2e-9-w", 4)


if __name__ == '__main__':
    o = LicenseKeyFormatting()
    o.run()
