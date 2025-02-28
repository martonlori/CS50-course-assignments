





def main():
    text = input("Input: ")
    word = shorten(text)
    print(word)

def shorten(word):
    new_text = []
    for i in word:
        if i not in ["a", "e", "i", "o", "u", "A", "E", "I", "U", "O"]:
            new_text.append(i)


    return "".join(new_text)


if __name__ == "__main__":
    main()
