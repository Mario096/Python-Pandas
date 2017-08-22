# Ankita Nayak , Lina Lopez, Mario Luevano
# lnl445
# MIS 304
# Dantu
# 04045

def main():

    #print the title and subsequent lines
    print("Welcome to Temperature Conversion Program")
    print("")
    print("1) Convert from Fahrenheit to Celsius")
    print("2) Convert from Celsius to Fahrenheit")


    #Get the user input
    choice = int(input("Enter your choice: "))
    temp = float(input("Enter the temperature: "))


    #Convert the temp to the Fahrenheit or Celsius
    if (choice == 1):
        temp_converted = (5/9)*(temp - 32)

        message = ("%.2f degrees Fahrenheit is equal to %.2f degrees Celsius" %(temp,temp_converted))
    else:
        temp_converted = (temp * (9/5)) + 32

        message = ("%.2f degrees Celsius is equal to %.2f degrees Fahrenheit" %(temp,temp_converted))

    #print the statements
    print("You selected Option", choice)
    print(message)




#call main
main()

