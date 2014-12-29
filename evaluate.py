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
    string = md(string)
    return string


def md(string):
    if "*" in string or "/" in string:
        mindex = -1
        dindex = -1
        if "*" in string:
            mindex = string.index("*")
        if "/" in string:
            dindex = string.index("/")
        if mindex == -1:
            if float(evaluate(string[dindex+1:])) == 0.0:
                print("Error: Cannot divide by 0")
                main()
                return
            return str(float(evaluate(string[:dindex]))/float(evaluate(string[dindex+1:])))
        if dindex == -1:
            return str(float(evaluate(string[:mindex]))*float(evaluate(string[mindex+1:])))
    else:
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
