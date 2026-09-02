class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = "({["
        closed = ")}]"
        for char in s:
            if char in opened:
                stack.append(char)
            elif char in closed:
                if not stack:
                    return False
                candidate = stack.pop()
                if char == ")":
                    if candidate == "(":
                        continue
                    else:
                        return False
                elif char == "}":
                    if candidate == "{":
                        continue
                    else:
                        return False
                elif char == "]":
                    if candidate == "[":
                        continue
                    else:
                        return False
        if stack:
            return False
        return True

            
        
        