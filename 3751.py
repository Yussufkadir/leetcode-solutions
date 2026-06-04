def totalWaviness(self, num1: int, num2: int) -> int:
    def count_up_to(x: int) -> int:
        s = str(x)
        n = len(s)
        from functools import lru_cache

        @lru_cache(None)
        def dp(pos: int, prev1: int, prev2: int, tight: bool, started: bool):
            if pos == n:
                return (1, 0)  
            limit = int(s[pos]) if tight else 9
            total_cnt = 0
            total_wav = 0
            for d in range(limit + 1):
                ntight = tight and (d == limit)
                nstarted = started or (d != 0)
                if not nstarted:
                    cnt, wav = dp(pos + 1, 10, 10, ntight, False)
                    total_cnt += cnt
                    total_wav += wav
                else:

                    new_prev1 = d
                    new_prev2 = 10 if prev1 == 10 else prev1
                    if prev1 != 10 and prev2 != 10:
                        is_peak = (prev2 < prev1 > d)
                        is_valley = (prev2 > prev1 < d)
                        extra = 1 if (is_peak or is_valley) else 0
                    else:
                        extra = 0
                    cnt, wav = dp(pos + 1, new_prev1, new_prev2, ntight, nstarted)
                    total_cnt += cnt
                    total_wav += wav + extra * cnt
            return (total_cnt, total_wav)

        _, waviness = dp(0, 10, 10, True, False)
        return waviness

    return count_up_to(num2) - count_up_to(num1 - 1)    