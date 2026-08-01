class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        trackCount = defaultdict(int)

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            trackCount[prereq[0]] += 1

        finished = 0

        dfs = []

        for i in range(numCourses):
            if trackCount[i] == 0:
                dfs.append(i)

        while len(dfs) > 0:
            curr = dfs.pop(-1)

            finished += 1

            for item in graph[curr]:
                trackCount[item] -= 1

                if trackCount[item] == 0:
                    dfs.append(item)

        return finished == numCourses

            