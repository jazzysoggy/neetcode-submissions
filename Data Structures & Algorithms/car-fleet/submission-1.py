class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        grouped = [(position[i], speed[i]) for i in range(len(position))]

        grouped.sort(reverse=True)

        prevTime = (target - grouped[0][0]) / grouped[0][1]
        fleet = 1
        for i in range(1, len(position)):
            curTime = (target - grouped[i][0]) / grouped[i][1]

            if curTime > prevTime:
                fleet += 1
                prevTime = curTime

        return fleet