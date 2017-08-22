#Define main
def main():
    message = "Athlete     Min    Max    Avg\n"

#get user input on number of athletes
    number = input("Enter the number of athletes practicing:")
#validate user input
    while not (number.isdigit()):
        print("Number of athletes must be an integer")
        number = input("Enter the number of athletes practicing:")

    number = int(number)

    for num in range(number):
        print()
        name = input("Enter the name of the athlete " + str(num +1) + ":")
        print()
        message += '{:<12}'.format(name)

#Get user input on minutes and seconds
        minutes,seconds = eval(input("Enter " + name + "'s  timing for 1000 meters or -1,-1 to quit (minutes,seconds):"))
        count = 0
        init_time = (60 * minutes) + seconds

        max_time = init_time
        min_time = init_time
        total_time = 0

        while minutes != -1 and seconds != -1:
            count +=1
            time = (60 * minutes) + seconds

            total_time += time
            avg = total_time/count

            if time > max_time:
                max_time = time
            elif time < min_time:
                min_time = time
            else:
                max_time = max_time
                min_time = min_time

            print()
            minutes,seconds = eval(input("Enter " + name + "'s  timing for 1000 meters or -1,-1 to quit (minutes,seconds):"))


        min_minutes = min_time // 60
        min_seconds = min_time % 60

        max_minutes = max_time // 60
        max_seconds = max_time % 60

        avg_minutes = avg // 60
        avg_seconds = avg % 60

        message += "%d:%d%4d:%d%4d:%d\n" %(min_minutes,min_seconds,max_minutes,max_seconds,avg_minutes,avg_seconds)
    print()
    print(message)


main()