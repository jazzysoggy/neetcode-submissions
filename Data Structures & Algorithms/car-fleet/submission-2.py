class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]

        pair.sort(reverse=True)

        fleet = 1
        latest_time = pair[0][1]

        for i in range(1, len(pair)):
            if pair[i][-1] > latest_time:
                latest_time = pair[i][-1]
                fleet += 1

        return fleet

