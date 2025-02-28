def main():

    grocery_list = {}


    while True:
        try:
            item = (input("")).upper()
            if item in grocery_list:
                grocery_list.update({f"{item}": f"{(int(grocery_list[item])) + 1}"})
            else:
                grocery_list[f"{item}"] = '1'

        except EOFError:

            for i in sorted(grocery_list):
                print(f"{grocery_list[i]}", i)
            break
        except:
            continue








main()
