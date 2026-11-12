class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ma = intervals[0][1]
        result = [intervals[0]]
        cur = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ma:
                result[cur][1] = max(result[cur][1], intervals[i][1])
                ma = max(result[cur][1], intervals[i][1])
            else:
                cur += 1
                ma = intervals[i][1]
                result.append(intervals[i])
        return result
        