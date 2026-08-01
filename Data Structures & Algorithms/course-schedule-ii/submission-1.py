class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []

        dfs = []

        graph = defaultdict(list)

        courseCount = defaultdict(int)

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            courseCount[prereq[0]] += 1


        for i in range(numCourses):
            if courseCount[i] == 0:
                dfs.append(i)

        while len(dfs) > 0:
            curr = dfs.pop()

            output.append(curr)

            for item in graph[curr]:
                courseCount[item] -= 1

                if courseCount[item] == 0:
                    dfs.append(item)


        return output if len(output) == numCourses else []


        



        