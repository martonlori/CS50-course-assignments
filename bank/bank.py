def main():
    greeting = input("Greeting: ").strip().lower()

    if greeting.find("hello") == 0:
        print("$0")
    elif greeting.find("h") == 0:
        print("$20")
    else:
        print("$100")



main()
