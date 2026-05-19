class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        trackCounts = defaultdict(int)

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            trackCounts[num] += 1

            freq[trackCounts[num]].append(num)

        i = -1
        output = set()
        while k > 0 and i >= -len(nums):
            for num in freq[i]:
                if num not in output:
                    output.add(num)
                    k -= 1
            i -= 1
            

        return list(output)
