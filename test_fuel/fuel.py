def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
        try:
            fraction = fraction.split("/")
            x,y=int(fraction[0]), int(fraction[1])
            # if x > y:
            #         raise ValueError("Numerator cannot be greater than denominator")
        except (ValueError,ZeroDivisionError,UnboundLocalError):
                raise
        else:
            return round(x/y * 100)



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
