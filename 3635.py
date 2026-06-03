from typing import List
import bisect

def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
    INF = 10**18
    land = sorted(zip(landStartTime, landDuration))
    n = len(land)
    land_start = [x[0] for x in land]
    land_dur   = [x[1] for x in land]
    land_sum   = [land_start[i] + land_dur[i] for i in range(n)]

    pref_land_dur = [0] * n
    pref_land_dur[0] = land_dur[0]
    for i in range(1, n):
        pref_land_dur[i] = min(pref_land_dur[i-1], land_dur[i])

    suff_land_sum = [0] * n
    suff_land_sum[n-1] = land_sum[n-1]
    for i in range(n-2, -1, -1):
        suff_land_sum[i] = min(suff_land_sum[i+1], land_sum[i])

    water = sorted(zip(waterStartTime, waterDuration))
    m = len(water)
    water_start = [x[0] for x in water]
    water_dur   = [x[1] for x in water]
    water_sum   = [water_start[i] + water_dur[i] for i in range(m)]

    pref_water_dur = [0] * m
    pref_water_dur[0] = water_dur[0]
    for i in range(1, m):
        pref_water_dur[i] = min(pref_water_dur[i-1], water_dur[i])

    suff_water_sum = [0] * m
    suff_water_sum[m-1] = water_sum[m-1]
    for i in range(m-2, -1, -1):
        suff_water_sum[i] = min(suff_water_sum[i+1], water_sum[i])

    ans = INF

    for i in range(n):
        sL, dL = land[i]
        T = sL + dL                    

        idx = bisect.bisect_left(water_start, T)
        if idx < m:
            ans = min(ans, suff_water_sum[idx])  

        if idx > 0:
            min_dur = pref_water_dur[idx-1]
            ans = min(ans, T + min_dur)

    for j in range(m):
        sW, dW = water[j]
        T = sW + dW                     

        idx = bisect.bisect_left(land_start, T)
        if idx < n:
            ans = min(ans, suff_land_sum[idx])

        if idx > 0:
            min_dur = pref_land_dur[idx-1]
            ans = min(ans, T + min_dur)

    return ans
        