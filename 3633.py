from typing import List
def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
    best = float('inf')
    for i in range(len(landStartTime)):
        for j in range(len(waterStartTime)):
            finish_land = landStartTime[i] + landDuration[i]
            start_water = max(waterStartTime[j], finish_land)
            finish = start_water + waterDuration[j]
            best = min(best, finish)

            finish_water = waterStartTime[j] + waterDuration[j]
            start_land = max(landStartTime[i], finish_water)
            finish = start_land + landDuration[i]
            best = min(best, finish)
    return best