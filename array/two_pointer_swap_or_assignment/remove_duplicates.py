class RemoveDuplicates:
    def __init__(self):
        """
        Given a sorted array, remove the duplicates in-place
        such that each element appear only once and return the new length.

        * - 限制条件：
        *   1. Do not allocate extra space.
        *   2. 结果可以是将 remove 掉的元素放在数组尾部，不需要硬删除。
        *   3. 除了被 remove 掉的元素之外，其他元素的相对顺序不能变。

        """
        self.array = [1, 1, 1, 2, 3, 4, 4, 7]

    def run(self):
        print(self.__class__.__name__)
        self.dedup()
        print(f"result_array: {self.array}")

    def dedup(self):
        start_index = 0
        for current_index in range(1, len(self.array)):
            if self.array[start_index] >= self.array[current_index]:
                temp_idx = current_index
                while temp_idx < len(self.array):
                    if self.array[start_index] < self.array[temp_idx]:
                        break
                    else:
                        temp_idx = temp_idx + 1
                if temp_idx < len(self.array):
                    self.array[current_index] = self.array[temp_idx]
            start_index += 1


if __name__ == '__main__':
    o = RemoveDuplicates()
    o.run()
