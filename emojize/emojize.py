import emoji

def main():
    try:
        text = input("Input: ")
        print(f"Output: {emoji.emojize(text, language="alias")}")
    except:
        print("Invalid input")






main()
