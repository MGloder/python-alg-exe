class ClimbingStairs:
    def __init__(self):
        """
        * - You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb
        *   1 or 2 steps. In how many distinct ways can you climb to the top? Note: n > 0.
        """
        self.num_of_stairs = 6

    def count_distinct_way_of_climbs(self):
        if self.num_of_stairs < 2:
            return 1
        if self.num_of_stairs < 3:
            return 2

        x = [0] * self.num_of_stairs
        x[0] = 1
        x[1] = 1
        for i in range(2, self.num_of_stairs):
            x[i] = x[i - 1] + x[i - 2]

        return x[self.num_of_stairs - 1]

    def run(self):
        count = self.count_distinct_way_of_climbs()
        print(f"{count}")


if __name__ == "__main__":
    o = ClimbingStairs()
    o.run()
