#Programmer: Suren Raj Tualdhar
#Date:13/07/2022
#Program: Switcback Nepal MTB Service Information

name = str(input("Enter the name"))
exp = int(input("Enter your Experience"))
if(exp > 2 ):
    print ("You are eligible for using our service")
    print ("Enter your choice from 1 to 5")
    print ("Choice 1: Bike Rental Charge Per Hour")
    print ("Choice 2: Shuttle Service Rate")
    print ("Choice 3: Accommodation Rate")
    print ("Choice 4: Heli Biking Rate")

    choice= int(input("Enter your choice"))
    if (choice== 1):
        print("The Bike rental charger per hour Is $20")
    elif (choice == 2):
        print("The shuttle service rate per trip is $50")
    elif (choice == 3):
        print("The accommodation rate per day is $ 150")
    elif (choice == 4):
        print("The heli biking rate per drop is $250")
else:
        print(Your are not eligible")
        print("Thank you choosing our Serivce")
        print("Visit Soon")

