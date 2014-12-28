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
    
    string = string.strip().replace(' ', '') #removes spaces, tabs, newlines
    
    if string == "back()": #Go back
        iqMath.main()
        
    if complete(string): #Check if there are empty 
        return string

    string = peval(string) #scans for parentheses and evaluates them
    return string


def peval(string):
    if "(" in string:
        if ")" in string[::-1]:
            temp = string[string.index('(')+1:len(string) - string[::-1].index(')')-1]
            return string[0:string.index('(')] + evaluate (temp) + string[len(string) - string[::-1].index(')')+1:]
        else:
            print("Error: Did not enclose parentheses. Try again!")
            main()

    if ")" in string:
        print("Error: Unexpected ')'.")
        main()
    else:
        return string


def complete(string):
    operations = list("+-*/")
    literal = True
    
    for item in operations: #Are there unperformed operations?
        if item in string:
            literal = False
    if not string[0].isdigit(): #Are there functions or uresolved variables?
        literal = False

    return literal
