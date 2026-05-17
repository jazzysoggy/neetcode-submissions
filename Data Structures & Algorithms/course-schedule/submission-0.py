class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseGraph = defaultdict(list)
        reqCount = defaultdict(int)

        for prereq in prerequisites:
            courseGraph[prereq[1]].append(prereq[0])
            reqCount[prereq[0]] += 1

        stack = deque()

        for i in range(numCourses):
            if reqCount[i] == 0:
                numCourses -= 1
                stack.append(i)

        while len(stack) != 0:
            curr = stack[0]
            stack.popleft()

            for item in courseGraph[curr]:
                reqCount[item] -= 1
                if reqCount[item] == 0:
                    stack.append(item)
                    numCourses -= 1

        return numCourses == 0