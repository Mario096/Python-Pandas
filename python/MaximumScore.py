# Ankita Nayak , Lina Lopez, Mario Luevano
# lnl445
# MIS 304
# Dantu
# 04045



def main():
    #declare max variable
    max = 0

    #ask for five separate IDs, names and scores
    id_1, score_1 = eval(input("Enter student id and score: "))
    name_1 = input("Enter student name: ")

    id_2, score_2 = eval(input("Enter student id and score: "))
    name_2 = input("Enter student name: ")

    id_3, score_3 = eval(input("Enter student id and score: "))
    name_3 = input("Enter student name: ")

    id_4, score_4 = eval(input("Enter student id and score: "))
    name_4 = input("Enter student name: ")

    id_5, score_5 = eval(input("Enter student id and score: "))
    name_5 = input("Enter student name: ")

    #determine which score is the maximum score
    #using if statements
    if (score_1> max ):
        max = score_1
        id_prime = id_1
        name_prime = name_1
    if(score_2 > max):
        max = score_2
        id_prime = id_2
        name_prime = name_2
    if(score_3 > max):
        max = score_3
        id_prime = id_3
        name_prime = name_3
    if(score_4 > max):
        max = score_4
        id_prime = id_4
        name_prime = name_4
    if(score_5 > max):
        max = score_5
        id_prime = id_5
        name_prime = name_5

    #print the maximum score with the name of
    #the student and the ID
    print("")
    print("Maximum score: ",max)
    print("Student id: ", id_prime)
    print("Student name: ", name_prime)
    
    
#call main
main()