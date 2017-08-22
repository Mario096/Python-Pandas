#import random library 
import random

#define second largest function
def secondlargest(list1):
    #set counter 
    max = 0
    for i in range(len(list1)):
        if list1[i] >= max:
            max = list1[i]

    list2 = [0 if x == max else x for x in list1]

    max2 = 0
    for j in range(len(list2)):
        if list2[j] > max2:
            max2 = list2[j]

    #return second largest function
    return max2
#define indsecmax fuction
def indsecmax(list1):
    max2 = secondlargest(list1)

    list2 = [0 if x == max else x for x in list1]
#return function
    return list2.index(max2)
#define main function
def main():

    list1 = []
    for i in range(10):
        x = random.randint(1,20)
        list1.append(x)

    listints = ''
    for j in range(len(list1)):
        if j != len(list1) - 1:
            listints += str(list1[j]) + "; "
        else:
            listints += str(list1[j])

    #Print statements 
    print("List of integers: ", listints)
    print("Second largest number:", secondlargest(list1))
    print("Index (position) of second largest number: ", indsecmax(list1))







#define main function 
main()
