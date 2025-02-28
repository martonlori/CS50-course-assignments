from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()


    if len(sys.argv) == 1:
         figlet.setFont(font=random.choice(fonts))
         text = input("Input: ")
         print(figlet.renderText(text))

    elif len(sys.argv) == 3:
         if not (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
              print("Invalid usage")
              sys.exit("Invalid usage")
         elif not ((sys.argv[2]) in fonts):
              print("Invalid usage")
              sys.exit("Invalid usage")
         else:
              text = input("Input: ")
              figlet.setFont(font=sys.argv[2])
              print(figlet.renderText(text))

    else:
         print("Invalid usage")
         sys.exit("Invalid usage")







main()
