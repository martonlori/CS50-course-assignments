def main():
    print(convert_faces(get_input()))


def get_input():
    user_input = input("Please enter a text ending with an face: ")
    return user_input

def convert_faces(user_input):
    replaced_text = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return replaced_text

main()
