class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n=len(s)
        ans=""
        for i in range(n):
            for j in range(i+1,n+1):
                sub=s[i:j]
                count=0
                for k in sub:
                    if k.lower() in sub and k.upper() in sub:
                        count+=1
                if count==len(sub):
                    if len(sub)>len(ans):
                        ans=sub
        return ans
        