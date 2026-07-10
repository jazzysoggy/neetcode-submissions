class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        test = 0

        for num in digits:
            test *= 10
            test += num
        
        test += 1

        output = list(str(test))

        for i in range(len(output)):
            output[i] = int(output[i])

        return output
