class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutationTracker = defaultdict(int)
        count = 0

        for char in s1:
            permutationTracker[char] += 1
            if permutationTracker[char] == 1:
                count += 1

        l = 0
        for i in range(len(s2)):
            char = s2[i]

            permutationTracker[char] -= 1

            if i - l >= len(s1):
                permutationTracker[s2[l]] += 1

                if permutationTracker[s2[l]] == 1:
                    count += 1

    
                l += 1

            if permutationTracker[char] == 0:
                count -= 1

                if count == 0:
                    return True


        return False