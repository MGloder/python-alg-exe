class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(num):
            for index_from_back in range(len(num) - 1, 0, -1):
                if num[index_from_back] > num[index_from_back - 1]:
                    index_from_back_str = ''.join(sorted(num[index_from_back:]))
                    print(index_from_back_str)
                    swapped_str = index_from_back_str[0] + num[index_from_back - 1] + index_from_back_str[1:]
                    num = num[:index_from_back - 1] + swapped_str
                    return num

            return num[::-1]

        original_num = num
        for num_of_run in range(0, k):
            num = next_permutation(num)

        orig = list(original_num)
        nums = list(num)
        i = 0
        count = 0
        print(orig)
        print(nums)

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
