def totalWaviness(self, num1: int, num2: int) -> int:
    def total_up_to(n: int) -> int:
        if n <= 0:
            return 0
        s = str(n)
        digits = list(map(int, s))
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(pos: int, tight: bool, started: bool, prev1: int, prev2: int):
            if pos == len(digits):
                return (1 if started else 0, 0)

            limit = digits[pos] if tight else 9
            total_cnt = 0
            total_wav = 0

            for d in range(limit + 1):
                new_tight = tight and (d == limit)
                new_started = started or (d != 0)

                if new_started:
                    if not started:
                        new_prev1 = d
                        new_prev2 = -1
                        add = 0
                    else:
                        new_prev2 = prev1
                        new_prev1 = d
                        if prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                                add = 1
                            else:
                                add = 0
                        else:
                            add = 0
                else:
                    new_prev1 = -1
                    new_prev2 = -1
                    add = 0

                cnt, wav = dfs(pos + 1, new_tight, new_started, new_prev1, new_prev2)
                total_cnt += cnt
                total_wav += wav + cnt * add

            return (total_cnt, total_wav)

        return dfs(0, True, False, -1, -1)[1]

    return total_up_to(num2) - total_up_to(num1 - 1)        