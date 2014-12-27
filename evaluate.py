"""
    file: evaluate.py
    author: Orens Xhagolli
    description: Evaluates a expression
"""

import iqMath


def main():
    expression = input("Please input the expression to evaluate: ")


def evaluate(string):
    operations = list("+-*/")
    breakable = False
    for item in operations:
        if item in string:
            breakable = True
    for char in string[0:3]:
        if char.isDigit():
            breakable = True

    if breakable == False:
        return string
