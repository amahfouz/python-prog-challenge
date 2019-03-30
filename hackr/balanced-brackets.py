#!/bin/python

OPEN_SET =  ['{', '[', '(']
CLOSE_SET = ['}', ']', ')']
CLOSE_MAP = {
    '{' : '}',
    '[' : ']',
    '(' : ')'
}

def is_balanced(string):
    stack = []
    for char in string:
        if char in OPEN_SET:
            stack.append(char)
        elif char in CLOSE_SET:
            if len(stack) == 0:
                return "NO"
            open_bracket = stack.pop()
            if CLOSE_MAP[open_bracket] != char:
                return False

    return len(stack) == 0

print is_balanced("{")