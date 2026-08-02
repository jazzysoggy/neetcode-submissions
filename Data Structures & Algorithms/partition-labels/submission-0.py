class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        trackCounts = defaultdict(int)

        for char in s:
            trackCounts[char] += 1

        trackSegment = defaultdict(int)
        incomplete = 0
        length = 0
        output = []

        for char in s:
            trackSegment[char] += 1
            length += 1

            if trackSegment[char] == 1:
                incomplete += 1

            if trackSegment[char] == trackCounts[char]:
                incomplete -= 1

            if incomplete == 0 and length > 0:
                output.append(length)
                length = 0
                trackSegment = defaultdict(int)

        return output