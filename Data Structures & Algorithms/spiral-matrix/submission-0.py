class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1

        while l <= r and t <= b:
            if t > b:
                break
            for j in range(l, r + 1):
                res.append(matrix[t][j])

            t += 1

            if l > r:
                break

            for i in range(t,b + 1):
                res.append(matrix[i][r])

            r -= 1

            if t > b:
                break

            for j in range(r, l - 1, -1):
                res.append(matrix[b][j])

            b -= 1

            if l > r:
                break

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])

            #[1,2,3,4]
            #[5,6,7,8]
            #[9,10,11,12]

            l += 1
        return res