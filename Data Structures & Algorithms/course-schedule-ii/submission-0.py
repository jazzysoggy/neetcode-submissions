class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outputOrder = []

        graph = defaultdict(list)

        prereqTrack = defaultdict(int)

        for prereq in prerequisites:
            prereqTrack[prereq[0]] += 1
            graph[prereq[1]].append(prereq[0])

        stack = deque()

        for i in range(numCourses):
            if prereqTrack[i] == 0:
                stack.append(i)

        while len(stack) > 0 :
            curr = stack[0]
            stack.popleft()

            outputOrder.append(curr)

            for item in graph[curr]:
                prereqTrack[item] -= 1
                if prereqTrack[item] == 0:
                    stack.append(item)

        return [] if len(outputOrder) != numCourses else outputOrder