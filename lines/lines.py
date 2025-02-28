import sys

def line_counter():
    lines_in_file = []
    lines_counter = 0


    if len(sys.argv) != 2:
        sys.exit("Specify a python file")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")
    else:
        try:
            with open(f"{sys.argv[1]}") as file:
                for line in file:
                    lines_in_file.append(line)
        except FileNotFoundError:
            sys.exit("Too few command line arguments")
        else:
            for i in lines_in_file:
                if i.strip().startswith("#"):
                    continue
                elif i.strip() == "\n":
                    continue
                elif i.strip() == "":
                    continue
                else:
                    lines_counter += 1

            return lines_counter


def main():
    #initiate an empty list to read lines from file
    #open the file, with an f string that lets user type in a python file
    #exclude comments and blank lines
    #if the file is not python file or no file was specified, sys.exit
    #elif output the no. lines in the file

    print(line_counter())

if __name__ == "__main__":
    main()
