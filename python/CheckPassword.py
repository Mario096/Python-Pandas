#define checkpassword function 
def checkPassword(password):
    valid = True
    if len(password) >= 8:
        valid = True
    else:
        valid = False


    spec = ["!","@","#","$","%","^","&","*","(",")"]

    d = 0
    upper = 0
    lower = 0
    special = 0
    for char in password:
        if char.isdigit():
            d += 1
        elif char.isalpha():
            if char.isupper():
               upper += 1
            else:
                lower += 1
        else:
            if char in spec:
                special += 1

    if valid and d >= 2 and upper >= 1 and lower >= 1 and special >= 1:
        valid = True
    else:
        valid = False

    return valid




#define main 
def main():
    #get input from user 
    password = str(input('Enter a password:'))

    result = checkPassword(password)

    #if statement to check valid
    if result == True:
        print("The result you entered is valid")
    else:
        print("The result you entered is invalid")

#call main 
main()
