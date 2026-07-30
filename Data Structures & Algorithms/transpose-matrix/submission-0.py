class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []

        for j in range(len(matrix[0])):
            output.append([])
            for i in range(len(matrix)):
                output[j].append(matrix[i][j])

        return output
            