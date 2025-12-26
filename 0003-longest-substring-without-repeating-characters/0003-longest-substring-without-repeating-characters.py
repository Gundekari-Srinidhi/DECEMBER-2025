class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        n=len(s)
        for i in range(n):
            ans=""
            for j in range(i,n):
                if s[j] in ans:
                    break
                ans+=s[j]
                max1=max(max1,j-i+1)
        return max1

        