class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        max1 = 0

        for i in range(n):
            d = {}
            for j in range(i, n):
                ch = s[j]
                if ch in d:
                    d[ch] += 1
                else:
                    d[ch] = 1

                length = j - i + 1

        
                if length < k or length <= max1:
                    continue

                valid = True
                for val in d.values():
                    if val < k:
                        valid = False
                        break

                if valid:
                    max1 = length

        return max1
