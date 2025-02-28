def main():
    text = input("camelCase: ").strip()
    new_text = []
    for i in text:
        if i.isupper():
            i = i.replace(i, f"_{i.lower()}")
            new_text.append(i)
        else:
            new_text.append(i)

    print("snake_case: " + "".join(new_text))







main()
