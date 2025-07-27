class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack and a hash map for matching brackets
        stack = []
        hash = {')': '(', ']': '[', '}': '{'}
        
        # Loop through each character in the string
        for char in s:
            if char in hash:
                # If it's a closing bracket, check the stack
                if stack and stack[-1] == hash[char]:
                    stack.pop()  # Remove the matching opening bracket
                else:
                    return False  # Invalid if no match
            else:
                # Push opening brackets onto the stack
                stack.append(char)
        
        # Return True if stack is empty, False otherwise
        return not stack