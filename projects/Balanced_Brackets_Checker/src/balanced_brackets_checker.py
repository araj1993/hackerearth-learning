"""
This function checks if the brackets in a given string are balanced.
It supports three types of brackets: (), {}, and [].

Input: A string containing brackets.
Output: "Balanced" if the brackets are balanced, otherwise "Not Balanced".

Example:
    is_balanced("(){}[]")  # Balanced
    is_balanced("([{}])")   # Balanced
    is_balanced("(}")       # Not Balanced
    is_balanced("((())")    # Not Balanced
"""

def is_balanced(input_string):

    stack = []
    
    if not any(bracket in input_string for bracket in "(){}[]"):
         return "Include brackets in the string"
    
    for each in input_string:
        if each in "({[":
            stack.append(each)
        elif each in ")}]":
            if not stack:
                return "Not Balanced"
            top = stack.pop()
            if (top == '(' and each != ')') or \
               (top == '{' and each != '}') or \
               (top == '[' and each != ']'):
                return "Not Balanced"

    return "Balanced" if not stack else "Not Balanced"

print(is_balanced(input("Enter a string with brackets ((),{},[]): ")))

