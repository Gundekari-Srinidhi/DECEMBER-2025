class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        n1=len(s1)
        n2=len(s2)
        for i in range(n2):
            if s1==sorted(s2[i:n1+i]):
                return True
        return False
        