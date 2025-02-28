def main():
    answer = input("What time is it? ")
    time = convert(answer)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")



def convert(time):
    hours_raw, minutes_raw = time.split(":")
    hours = int(hours_raw)
    minutes = int(minutes_raw)
    if hours > 24:
        hours = 24
    elif hours < 0:
        hours = 0

    minutes = minutes * 60 / 3600
    result = hours + minutes
    return (result)



if __name__ == "__main__":
    main()
