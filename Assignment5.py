def training():
    print("Hello! welcome to this exercise!")
    x = int(input("Would you like to enter data for a training run? Enter 0 if no. Enter 1 if yes: "))
    if x == 0:
        return"Have a good day!"
    if x == 1:
        k = 1
        minutes = 0
        mileage = 0
        mileCount = 0
        frequency = 0
        maxMile = 0
        paceCount = 0
        while(k == 1):
            mileage = int(input("Enter the distance ran in miles: "))
            minutes = int(input("Enter the time needed to run the milage, in minutes: "))
            frequency += 1
            mileCount += mileage
            if mileage > maxMile:
                maxMile = mileage
            pace = minutes/mileage
            pacecount += pace
            print("Your pace is " + str(pace))
            k = int(input("Would you like to add more? enter 1 if yes enter 0 if no: "))
        print("Your total number of training runs entered is " + str(frequency))
        print("Your total mileage of all your runs is " + str(mileCount))
        print("The longest mile that you ran is " + str(maxMile))
        avgPace = paceCount / frequency
        print("Your average pace is " + str(avgPace))
training()
