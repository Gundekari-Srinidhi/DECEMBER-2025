class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)
        l=[]
        p_sort=sorted(p)
        for i in range(n-m+1):
            sub=s[i:m+i]
            if sorted(sub)==p_sort:
                l.append(i)
        return l

        