class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(bool)
        trusted = defaultdict(int)

        for trustee in trust:
            trusts[trustee[0]] = True
            trusted[trustee[1]] += 1

        output = -1

        for i in range(1, n + 1):
            if not trusts[i] and trusted[i] == n - 1:
                if output != -1:
                    return -1
                
                output = i

        return output