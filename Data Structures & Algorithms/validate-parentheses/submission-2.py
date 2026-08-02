class Solution:
    def isValid(self, s: str) -> bool:
        trackPara = []

        for i in s:
            if i == '[' or i == '(' or i == '{':
                trackPara.append(i)
            elif i == ']':
                if len(trackPara) == 0 or trackPara[-1] != '[':
                    return False
                
                trackPara.pop()

            elif i == ')':
                if len(trackPara) == 0 or trackPara[-1] != '(':
                    return False
                
                trackPara.pop()
            elif i == '}':
                if len(trackPara) == 0 or trackPara[-1] != '{':
                    return False
                
                trackPara.pop()

        return len(trackPara) == 0

