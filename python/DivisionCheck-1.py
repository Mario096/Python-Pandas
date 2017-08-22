# Ankita Nayak , Lina Lopez, Mario Luevano
# lnl445
# MIS 304
# Dantu
# 04045


def main():

    #Get the integer from the user
    number = int(input("Enter an integer:"))

    #Determine if the integer is divisible by 2 or 3, neither or both

    if ((number % 2 == 0) and (number % 3 == 0)):
        message = "by both 2 and 3"
    elif (number % 2 == 0):
        message = "by 2 but not 3"
    elif (number % 3 == 0):
        message = "by 3 but not 2"
    else:
        message = "neither by 2 nor by 3"

    #print the message out
    print("Number", number,"is divisible", message)

#call main
main()
