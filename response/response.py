from validator_collection import checkers


def main():
    if checkers.is_email(input("Email: ")) == True:
        print('Valid')
    else:
        print('Invalid')






main()
