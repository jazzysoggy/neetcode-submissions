class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        newTaskList = []

        for i in range(len(tasks)):
            heapq.heappush(newTaskList, tuple(tasks[i] + [i]))

        toProcess = []

        time = 0

        ans = []

        while len(toProcess) + len(newTaskList) != 0:
            while len(newTaskList) > 0 and time >= newTaskList[0][0]:
                heapq.heappush(toProcess, (newTaskList[0][1], newTaskList[0][2]))
                heapq.heappop(newTaskList)
            
            if len(toProcess) != 0:
                (a,b) = heapq.heappop(toProcess)

                time = time + a

                ans.append(b)

            if len(newTaskList) != 0:
                time = max(time, newTaskList[0][0])

        return ans



            