#define Product Price function
def getProductPrice(product_code):

    if product_code == 1:
        price = 2.98
    elif product_code == 2:
        price = 4.50
    elif product_code == 3:
        price = 9.98
    elif product_code == 4:
        price = 4.49
    else:
        price = 6.87

    return price

#Function to find total price after quantity, product price, and discounts
def displayTotalPrice(product_quantity, product_price, membership_indicator):

    valentines_discount = .05 * (product_price * product_quantity)
    member_discount = .05 * (product_price * product_quantity)

    if membership_indicator == "y":
        Total_price = (product_quantity * product_price) - (member_discount + valentines_discount)
    else:
        Total_price = (product_quantity * product_price) - valentines_discount

    return Total_price


#define main
def main():
#Print Header
    message = "Welcome to the Online Retail Store\n"
    message += "---------------------------------"

    print(message)
#Get input form user on product code number
    product_code = int(input("Enter the product code: "))
#While loop to validate input
    while 0 >= product_code or product_code >= 6:
        print("Product code is invalid")
        product_code = int(input("Enter the product code: "))
#Receive input from user on quantity and membership status
    quantity = int(input("Enter the quantity required: "))
    member = input("Are you a member? (y / n):")


#Calculate outputs and print them out
    final_price = displayTotalPrice(quantity,getProductPrice(product_code),member)


    discount = (getProductPrice(product_code) * quantity) - final_price

    print()
    print("Your final price is: $%.2f" %final_price)
    print("Discount earned: $%.2f" %discount)



main()