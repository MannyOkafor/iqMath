"""
    file: iqMath.py
    author: Orens Xhagolli
    description: This does math! (Sorry for general description,
    I'm still not sure how far to take this)
"""

import evaluate
#import os #Optional if you want to use commands like "clear()"


def main():
    print("Welcome to iqMath!")
    print("Please choose what would you like to do next.")
    print("1. Evaluate an expression.")

    response = int(input("Enter number: ").strip())
    if response == 1:
        evaluate.main() #transfers control to the other file
    else:
        clear()
        main()
