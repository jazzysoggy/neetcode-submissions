class Solution:
    def reorganizeString(self, s: str) -> str:
        totalCount = defaultdict(int)

        for char in s:
            totalCount[char] += 1

        outputHeap = []

        for char in totalCount:
            heapq.heappush(outputHeap, (-totalCount[char], char))

        output = ""

        while len(outputHeap) > 0:
            count, char = heapq.heappop(outputHeap)

            if len(output) == 0 or output[-1] != char:
                output += char

                if count < -1:
                    heapq.heappush(outputHeap, (count + 1, char))
            
            elif len(outputHeap) > 0:
                count2, char2 = heapq.heappop(outputHeap)

                output += char2
                
                heapq.heappush(outputHeap, (count, char))

                if count2 < -1:
                    heapq.heappush(outputHeap, (count2 + 1, char2))

            else:
                return ""

        return output