class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        output = [0,0,0]

        for item in triplets:
            if item[0] > target[0] or item[1] > target[1] or item[2] > target[2]:
                continue

            output[0] = max(output[0], item[0])
            output[1] = max(output[1], item[1])
            output[2] = max(output[2], item[2])

        return target == output

            