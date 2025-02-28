def main():
    while True:
        try:
            fraction = input("Fraction: ").split("/")
            x,y=int(fraction[0]), int(fraction[1])
            if x > y:
                continue
        except (ValueError,ZeroDivisionError,UnboundLocalError):
            print("Please enter 2 integers")



        else:
            output = round(x / y * 100)

            if output <= 1:
                print("E")
                break
            elif output >= 99:
                print("F")
                break
            else:
                print(f"{output}%")
                break





main()
