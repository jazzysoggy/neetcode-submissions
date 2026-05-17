class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        banned = defaultdict(int)

        totalBanned = defaultdict(int)
        total = defaultdict(int)
        for senator in senate:
            total[senator] += 1

        valid = set("DR")

        senate = list(senate)
        
        while True:
            for i in range(len(senate)):
                senator = senate[i]
                if senator not in valid:
                    continue

                if banned[senator] > 0:
                    banned[senator] -= 1
                    senate[i] = "L"
                else:
                    if totalBanned["R" if senator == "D" else "D"] == total["R" if senator == "D" else "D"]:
                        return "Radiant" if senator == "R" else "Dire"
                    banned["R" if senator == "D" else "D"] += 1
                    totalBanned["R" if senator == "D" else "D"] += 1
                
        return "None"
            