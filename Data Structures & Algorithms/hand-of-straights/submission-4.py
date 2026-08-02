class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        item = Counter(hand)

        for i in hand:
            start = i
            while item[start - 1]:
                start -= 1

            while start <= i and item[start] > 0:
                print(item)
                for j in range(start, start + groupSize):
                    if not item[j]:
                        print(start, j)
                        print(item)
                        return False

                    item[j] -= 1

                if item[start] == 0:
                    start + 1

        return True