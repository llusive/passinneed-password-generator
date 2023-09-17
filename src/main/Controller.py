# This program is responsible for calling and returning the different methods of generating a password
# class Methods:
#     def alphaNumeric():

#     def lengthMethod():

#     def specialCharacters():


# This program is responsible for calling and returning the different methods of generating a password

if __name__ == "__main__":
# This program will temporarily use switch case as a substitution for buttons
    prompt = 0
    
    print("Password Generators")
    print("1. Alphanumeric Method")
    print("2. Length Method")
    print("3. Special Characters Method")
    print("4. Exit")
    prompt = input("Choose method [1-4]: ")
    
    while (prompt != '4'):
        if prompt == '1':
            print("This is an Alphanumeric Method")
            break
        elif prompt == '2':
            print("This is an Length Method")
            break
        elif prompt == '3':
            print("This is an Special Characters Method")
            break
        elif prompt == '4':
            print("Thank you for using our program :)")
            break
        else:
            print("Please choose an appropriate answer.")
            break