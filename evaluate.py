"""
    file: evaluate.py
    author: Orens Xhagolli
    description: Evaluates a expression
"""

import iqMath


def main():
    expression = 0
    while expression != "exit()":
        expression = input("Please input the expression to evaluate: ")
        print(evaluate(expression))


def evaluate(string):
    
    string = string.strip().replace(' ', '') #removes spaces, tabs, newlines
    
    if string == "back()": #Go back
        iqMath.main()
        
    if complete(string): #Check if there are empty 
        return string
    while "(" in string:
        string = peval(string) #scans for parentheses and evaluates them
    string = md(string)
    string = addsub(string)
    return string


def addsub(string):
    if "+" in string or "-" in string:
        arg1 = ""
        arg2 = ""
        oper = None
        i = 0
        while i < len(string):
            if string[i].isdigit() or string[i] == ".":
                if oper is None:
                    arg1 += string[i]
                else:
                    arg2 += string[i]
            else:
                if oper is None:
                    oper = string[i]
                else:
                    break
            i+=1
        if oper == "+":
            return evaluate(str(float(arg1)+float(arg2))+string[i:])
        elif oper == "-":
            return evaluate(str(float(arg1)-float(arg2))+string[i:])
    else:
        return string


def md(string):
    if "*" in string or "/" in string:
        i = len(string)-1
        oper = None
        while True:
            if string[i] == "*" or string[i] == "/":
                oper = string[i]
                break
            i -= 1
        if oper == "*":
            return str(float(evaluate(string[:i]))*float(evaluate(string[i+1:])))
        else:
            divisor = float(evaluate(string[i+1:]))
            if divisor == 0.0:
                print("Error: Can't divide by 0")
                main()
                return
            else:
                return str(float(evaluate(string[:i]))/divisor)
    else:
        return string


def peval(string):
    if "(" in string:
        openp = []
        closep = []
        for i in range(0, len(string)):
            if string[i] == "(":
                openp.append(i)
            elif string[i] == ")":
                closep.append(i)
        if len(closep) != len(openp):
            print("Error: Parenthesis missing")
            main()
        else:
            workindex = 0
            i = 0
            while i < len(openp):
                if openp[i] < closep[0]:
                    workindex = openp[i]
                i += 1
            return string[:workindex]+evaluate(string[workindex+1:closep[0]])+string[closep[0]+1:]

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
    if string is not None or string != "":
        if not string[0].isdigit(): #Are there functions or uresolved variables?
            literal = False

    return literal

main()
