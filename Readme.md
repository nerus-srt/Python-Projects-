# Switchback Nepal MTB Service Information

## Project Overview
**Project Name**: Switchback Nepal MTB Service Information  
**Objective**: To provide information about mountain biking services to users based on their experience.

## Project Requirements and Dependencies
- **Python**: Used to write the script.
- **No additional libraries required**.

## Steps

1. **User Input**:
   - Prompt the user to enter their name.
   - Prompt the user to enter their experience in years.

2. **Eligibility Check**:
   - Check if the user's experience is more than 2 years.
   - If eligible, proceed to service selection.

3. **Service Selection**:
   - Display a menu of service options:
     - Choice 1: Bike Rental Charge Per Hour
     - Choice 2: Shuttle Service Rate
     - Choice 3: Accommodation Rate
     - Choice 4: Heli Biking Rate
   - Prompt the user to select a service.

4. **Display Service Rates**:
   - Based on the user's choice, display the corresponding service rate.

5. **Ineligible Users**:
   - If the user is not eligible, display a message stating they are not eligible and thank them for choosing the service.

## Code

```python
# Programmer: Suren Raj Tuladhar
# Date: 13/07/2022
# Program: Switchback Nepal MTB Service Information

def get_user_input():
    name = input("Enter your name: ")
    exp = input("Enter your experience in years: ")
    return name, exp

def check_eligibility(exp):
    try:
        exp = int(exp)
        if exp > 2:
            return True
        else:
            return False
    except ValueError:
        print("Invalid input for experience. Please enter a number.")
        return False

def display_services():
    print("You are eligible for using our service")
    print("Enter your choice from 1 to 4")
    print("Choice 1: Bike Rental Charge Per Hour")
    print("Choice 2: Shuttle Service Rate")
    print("Choice 3: Accommodation Rate")
    print("Choice 4: Heli Biking Rate")

def get_service_choice():
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        return choice
    except ValueError:
        print("Invalid input for choice. Please enter a number.")
        return None

def display_service_rate(choice):
    if choice == 1:
        print("The Bike rental charge per hour is $20")
    elif choice == 2:
        print("The shuttle service rate per trip is $50")
    elif choice == 3:
        print("The accommodation rate per day is $150")
    elif choice == 4:
        print("The heli biking rate per drop is $250")
    else:
        print("Invalid choice. Please select a valid option from 1 to 4.")

def main():
    name, exp = get_user_input()
    if check_eligibility(exp):
        display_services()
        choice = get_service_choice()
        if choice is not None:
            display_service_rate(choice)
    else:
        print("You are not eligible")
        print("Thank you for choosing our service")
        print("Visit soon")

if __name__ == "__main__":
    main()
