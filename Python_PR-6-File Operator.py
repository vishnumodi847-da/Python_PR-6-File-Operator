# Project : File Operator
import os

file_name = "j.txt"

while True:
    print("\n----------Journal Entry----------")
    print("1. Add Entry.")
    print("2. View Entry.")
    print("3. Search Entry.")
    print("4. Delect Entry.")
    print("5.Exit.")

    choice = input("Enter Your Choice -- ")

    # Add Entry
    if choice == "1":
        try:
            entry = input("Write Your Entry -- ")
            with open(file_name, "a") as f:
                f.write(entry + "\n")
            print("Entry saved")
        except Exception as e:
            print("Error -- ", e)

    # View Entry
    elif choice == "2":
        try:
            with open(file_name, "r") as f:
                print("Your entries: \n")
                print(f.read())

        except Exception as e:
            print("Error -- ", e)

    # Search Entry
    elif choice == "3":
        
            word = input("Enter your Searching word -- ")
            with open(file_name, "r") as f:
                h=1
                for i in f:
                    if word in i:
                        print("Found in line ", h)
                    h = h + 1

    #Delete Entry
    elif choice == "4":
        try:
            os.remove(file_name)
            print("Deleted file ")

        except Exception:
            print("File not found")

    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invaild Choice")        
