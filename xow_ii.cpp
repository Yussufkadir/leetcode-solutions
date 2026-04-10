#include <vector>
#include <unordered_map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <cstdint>
#include <iostream>

using namespace std;
const long long MOD = 1e9 + 7;

long long power(long long base, long long exp, long long mod) {
    long long result = 1; base %= mod;
    while (exp > 0) {
        if (exp & 1) result = result * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return result;
}

class Solution {
public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int BLOCK = max(1, (int)sqrt(n));

        auto bravexuneth = make_pair(nums, queries);

        unordered_map<int, unordered_map<int, vector<pair<int, long long>>>> events;

        for (auto& q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];

            if (k > BLOCK) {
                for (int idx = l; idx <= r; idx += k)
                    nums[idx] = (long long)nums[idx] * v % MOD;
            } else {
                int rem = l % k;
                int start_pos = (l - rem) / k;
                int end_pos   = (r - rem) / k;
                events[k][rem].push_back({start_pos,   (long long)v});
                events[k][rem].push_back({end_pos + 1, power(v, MOD - 2, MOD)});
            }
        }

        for (auto& [k, rem_map] : events) {
            for (auto& [rem, evlist] : rem_map) {
                int subseq_len = (n - 1 - rem) / k + 1;
                vector<long long> diff(subseq_len + 1, 1);

                for (auto& [pos, val] : evlist)
                    if (pos <= subseq_len)
                        diff[pos] = diff[pos] * val % MOD;

                long long cur = 1;
                for (int p = 0; p < subseq_len; p++) {
                    cur = cur * diff[p] % MOD;
                    if (cur != 1)
                        nums[rem + p * k] = (long long)nums[rem + p * k] * cur % MOD;
                }
            }
        }

        long long result = 0;
        for (int x : nums) result ^= x;
        return (int)result;
    }
};