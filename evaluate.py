"""
    file: evaluate.py
    author: Orens Xhagolli
    description: Evaluates a expression
"""

import iqMath


def main():
    expression = input("Please input the expression to evaluate: ")
    evaluate(expression)


def evaluate(string):
    
    if string == "back()": #Go back
        iqMath.main()
        
    if complete(string): #Check if there are empty 
        return string

    peval(string) #scans for parentheses


def peval(string):
    pass


def complete(string):
    operations = list("+-*/")
    breakable = False
    for item in operations: #Are there unperformed operations?
        if item in string:
            breakable = True
    for char in string[0:3]: #Are there any functions being performed?
        if char.isDigit():
            breakable = True

    return not breakable
