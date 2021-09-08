class RemoveDuplicates:
    def __init__(self):
        """
        * Remove Duplicates II
        *
        * - Given a sorted array, remove the duplicates in-place such that duplicates appeared at most twice and
        *   return the new length (为有序数组去重，每个元素最多出现两次).
        * 思路： 通过双指针，去判断后面的第二位
        """
        self.array = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 7]

    def run(self):
        print(self.__class__.__name__)
        i = self.dedup()
        print(f"length: {i}")
        print(f"result_array: {self.array}")

    def dedup(self):
        validate_index = 0
        for index in range(0, len(self.array)):
            if index + 2 >= len(self.array):
                if index + 1 >= len(self.array):
                    return validate_index + 1
                return validate_index
            if self.array[index] == self.array[index + 2]:
                next_index = self.find_next_index(index + 2)
                if next_index != -1:
                    self.array[index + 2] = self.array[next_index]
                else:
                    return validate_index
                validate_index += 1
            else:
                validate_index += 1

    def find_next_index(self, index):
        for next_index in range(index + 1, len(self.array)):
            if self.array[index] != self.array[next_index]:
                return next_index
        return -1


if __name__ == '__main__':
    o = RemoveDuplicates()
    o.run()
