class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        _max = 1
        counter = {s[0]: 1}

        while r < len(s) - 1:
            r += 1
            counter[s[r]] = counter.get(s[r], 0) + 1

            while counter[s[r]] > 2:  
                counter[s[l]] -= 1
                l += 1
            
            _max = max(_max, r - l + 1) 

        return _max
