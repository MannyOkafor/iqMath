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
        arg1 = ""
        arg2 = ""
        a1index = 0
        a2index = 0
        oper = None
        for i in range(0,len(string)):
            if string[i].isdigit() or string[i] == ".":
                if oper is None:
                    arg1 += string[i]
                else:
                    arg2 += string[i]
                    a2index = i
            elif string[i] == "+" or string[i] == "-":
                if oper is None:
                    arg1 = ""
                    a1index = i+1
                else:
                    break
            else:
                if oper is None:
                    oper = string[i]
                else:
                    break
        if oper == "*":
            temp = evaluate(string[:a1index]+str(float(arg1) * float(arg2))+string[a2index:])
            return temp[:len(temp)-1] #-1 corrects for floating point arithmetic errors
        else:
            if float(arg2) == 0.0:
                print("Error: Cannot divide by 0")
                main()
                return
            temp = evaluate(string[:a1index]+str(float(arg1) / float(arg2))+string[a2index:])
            return temp[:len(temp)-1]
    else:
        return string


def peval(string):
    if "(" in string:
        if ")" in string[::-1]:
            temp = string[string.index('(')+1:len(string) - string[::-1].index(')')-1]
            cmplstr = string[:string.index(temp)-1]+evaluate(temp)+string[string.index(temp)+len(temp)+1:]
            if "(" in cmplstr:
                peval(cmplstr)
            else:
                return cmplstr
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
    if string is not None or string != "":
        if not string[0].isdigit(): #Are there functions or uresolved variables?
            literal = False

    return literal
