"""
    file: evaluate.py
    author: Orens Xhagolli
    description: Evaluates a expression
"""

import iqMath


def main():
    expression = input("Please input the expression to evaluate: ")
    print(evaluate(expression))


def evaluate(string):
    
    if string == "back()": #Go back
        iqMath.main()
        
    if complete(string): #Check if there are empty 
        return string

    peval(string) #scans for parentheses


def peval(string):
    return None


def complete(string):
    operations = list("+-*/")
    literal = True
    
    for item in operations: #Are there unperformed operations?
        if item in string:
            literal = False
    if not string[0].isdigit(): #Are there functions or uresolved variables?
        literal = False

    return literal
