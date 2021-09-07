class RemoveElements:
    def __init__(self):
        """
        * Remove Element
        *
        * - Given an array and a value, remove all instances of that value in-place and return the new length.
        *
        * - 限制条件：
        *   1. Do not allocate extra space.
        *   2. 结果可以是将 remove 掉的元素放在数组尾部，不需要硬删除。
        *   3. 除了被 remove 掉的元素之外，其他元素的相对顺序不能变。
        """
        self.array = [3, 2, 1, 4, 3, 5, 6, 3, 2, 1]
        pass

    def del_elem(self, val):
        validate_index = -1
        for index in range(0, len(self.array)):
            print(self.array)
            if self.array[index] == val:
                next_validate_index = -1
                for is_next_validate_index in range(index + 1, len(self.array)):
                    if self.array[is_next_validate_index] != val:
                        next_validate_index = is_next_validate_index
                        break
                if next_validate_index == -1:
                    break
                self.array[index] = self.array[next_validate_index]
                self.array[next_validate_index] = val

            validate_index += 1
        return validate_index

    def run(self):
        print(f"index: {self.del_elem(3)}")
        print(f"array: {self.array}")
        pass


if __name__ == '__main__':
    o = RemoveElements()
    o.run()
