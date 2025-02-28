def main():
    text = input("Input: ")
    new_text = []
    for i in text:
        if i not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            new_text.append(i)


    print("Output:", "".join(new_text))






main()
