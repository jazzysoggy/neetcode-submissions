class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()


        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                queue.append(s[i])
            else:
                if len(queue) == 0:
                    return False

                curr = queue.pop()

                string =curr + s[i]

                if string != '()' and string != '{}' and string !='[]':
                    return False


        return len(queue) == 0