def is_validate(value):
    return value != 0


class MoveZeros:
    def __init__(self):
        """
        * Move Zeroes
        *
        * - Given an array, move all 0's to the end of the array while maintaining the relative order of others.
        """
        self.array = [0, 1, 0, 2, 5, 0, 3, 2, 0, 0]
        """
        赋值补0
        """

    def run(self):
        self.move_zeros()
        print(f"move zeros {self.array}")

    def move_zeros(self):
        for index in range(0, len(self.array)):
            if is_validate(self.array[index]):
                continue
            next_validate_index = self.find_next_valdiate_index(index)
            if next_validate_index == -1:
                break
            self.array[index] = self.array[next_validate_index]
            self.array[next_validate_index] = 0

    def find_next_valdiate_index(self, index):
        for next_index in range(index + 1, len(self.array)):
            if is_validate(self.array[next_index]):
                return next_index
        return -1


if __name__ == '__main__':
    o = MoveZeros()
    o.run()
