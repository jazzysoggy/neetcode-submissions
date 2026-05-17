class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)

        for num in nums:
            table[num] += 1

        table = list(table.items())

        table = sorted(table, key=lambda x: -x[1])

        output = []
        i = 0
        while len(output) < k and i < len(table):
            output.append(table[i][0])
            i += 1

        return output
