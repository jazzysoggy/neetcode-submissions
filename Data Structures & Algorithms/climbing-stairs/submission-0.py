class Solution:
    def climbStairs(self, n: int) -> int:
        array = [0] * (n+1)

        array[0] = 1

        for i in range(1,len(array)):
            array[i] += array[i-1]

            if i-2 >= 0:
                array[i] += array[i-2]
        
        return array[-1]