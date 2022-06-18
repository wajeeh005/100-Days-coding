def leap_year():
    year= int(input("Which year do you want to check?   "))

    if year % 4 ==0:
        print("This is Leap Year.")
    else:
        print("This is not a leap year ")


leap_year()