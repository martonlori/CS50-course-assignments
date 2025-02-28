# def main():
#     txt = input().replace(" ", "...")
#     print(txt)

def main():
    print(slowdown(get_text()))


def get_text():
    txt = input()
    return txt

def slowdown(txt):
    slowed_down_text = txt.replace(" ", "...")
    return slowed_down_text

main()

