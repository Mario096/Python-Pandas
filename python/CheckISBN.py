#Lina Lopez lnl445

#Mario Luevano ml38994
#import system specefic module
import sys
#define main
def main():

    isbn = ''
    #while loop to check input validation 
    while isbn != "-1":
        #get input from user for isbn
        isbn = (input("Enter either 9 or 12 digits as a string (or -1 to quit):"))
        #inner loop 
        while len(isbn)!= 9:
            if len(isbn) == 12:
                break
            elif isbn == "-1":
                sys.exit()
            else:
                print()
                print("Invalid ISBN number.")
                isbn = (input("Enter either 9 or 12 digits as a string (or -1 to quit):"))
        #for loop to validate correct user input
        for i in range(len(isbn)):
            if not isbn[i].isdigit():
                print()
                print("Invalid ISBN number")
                isbn = (input("Enter either 9 or 12 digits as a string (or -1 to quit):"))

        #create a counter 
        checksum = 0

        if len(isbn) == 9:
            for i in range(len(isbn)):
                checksum += int(isbn[i]) * (int(i + 1))
            checksum = checksum % 11

        elif len(isbn) == 12:
            for i in range(len(isbn)):
                if int(i) % 2 == 1:
                    checksum += int(isbn[i])
                else:
                    checksum += int(isbn[i]) * 3
            checksum = 10 - checksum % 10

        if checksum == 10:
            if len(isbn) == 9:
                isbn += "X"
            elif len(isbn) == 12:
                isbn += "0"
        else:
            isbn += str(checksum)


        length = len(isbn)
        #print the output
        print("The ISBN-" +str(length), "number is: ", isbn, checksum)
        print()


main()