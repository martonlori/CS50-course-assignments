import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"^(?:<iframe).*(?:src=\")(?:http){1}s?://(?:www.)?(?:youtube\.com/embed/)(\w{11})\".*(?:</iframe>)$"
    matches = re.search(pattern,s)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
