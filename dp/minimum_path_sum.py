class MinimumPathSum:
    def __init__(self):
        """
        * - Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which
        *   minimizes the sum of all numbers along its path. Returns the sum at the end.
        * - Rule: You can only move either down or right at any point in time.
        """
        self.array = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 300, 4, 5],
            [1, 200, 3, 4, 5],
            [100, 2, 3, 4, 5]
        ]
        rows = len(self.array)
        cols = len(self.array[0])
        self.init_array = [[1000000000 for col in range(cols)] for row in range(rows)]

    def run(self):
        row = len(self.array) - 1
        col = len(self.array[row]) - 1
        self.get_minimum_path_sum(row, col)
        print(f"result: {self.init_array[row][col]}")

    def get_minimum_path_sum(self, row, col):
        if row > 0 and col > 0:
            x = self.getY(row - 1, col)
            y = self.getY(row, col - 1)
            self.init_array[row][col] = min(x, y) + self.array[row][col]
            return self.init_array[row][col]
        elif row > 0:
            self.init_array[row][col] = self.getY(row - 1, col) \
                                            + self.array[row][col]
            return self.init_array[row][col]
        elif col > 0:
            self.init_array[row][col] = self.getY(row, col - 1) \
                                            + self.array[row][col]
            return self.init_array[row][col]
        return self.array[row][col]

    def getY(self, row, col):
        if self.init_array[row][col] != 1000000000:
            return self.init_array[row][col]
        else:
            return self.get_minimum_path_sum(row, col)


if __name__ == '__main__':
    o = MinimumPathSum()
    o.run()
