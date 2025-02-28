def main():
    file_name = input("File name: ").strip().lower()

    if not (file_name.endswith(".gif") == True or file_name.endswith(".jpg") == True or file_name.endswith(".jpeg") == True or file_name.endswith(".png") == True or file_name.endswith(".pdf") == True or file_name.endswith(".txt") == True or file_name.endswith(".zip") == True):
        print("application/octet-stream")
    elif file_name.endswith(".gif") == True:
        print("image/gif")
    elif file_name.endswith(".jpg") == True:
        print("image/jpeg")
    elif file_name.endswith(".jpeg") == True:
        print("image/jpeg")
    elif file_name.endswith(".png") == True:
        print("image/png")
    elif file_name.endswith(".pdf") == True:
        print("application/pdf")
    elif file_name.endswith(".txt") == True:
        print("text/plain")
    elif file_name.endswith(".zip") == True:
        print("application/zip")


main()
