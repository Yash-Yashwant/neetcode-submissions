class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD = {}
        tD = {}

        for i in s:
            sD[i] = sD.get(i, 0) + 1
        for j in t:
            tD[j] = tD.get(j, 0) + 1
        return sD == tD
            

    