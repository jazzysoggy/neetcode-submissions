class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        track = defaultdict(int)

        count = 0
        for char in s1:
            track[char] += 1
            count += 1

        left = 0

        for right in range(len(s2)):
            if (right - left >= len(s1)):
                track[s2[left]] += 1
                count += 1
                left += 1

            track[s2[right]] -= 1
            count -= 1

            while (track[s2[right]] < 0):
                track[s2[left]] += 1
                left += 1
                count += 1


            if(count == 0):
                return True
            

        return False