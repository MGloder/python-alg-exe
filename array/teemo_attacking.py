class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) <= 0:
            return 0

        timer_start_point = timeSeries[0]
        total_time = 0
        for i in range(1, len(timeSeries)):
            if timer_start_point + duration - 1 < timeSeries[i]:
                total_time += duration
            else:
                total_time += timeSeries[i] - timer_start_point
            timer_start_point = timeSeries[i]

        return total_time + duration
