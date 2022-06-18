def tip_calculator():
    print("Hello Welcome to Tip calculator")
    total_bill =int(input("What is your total bill?     "))
    percentage_of_bill= int(input("What percentage you like? 10,12 or 15     "))
    total_no_of_peoples_to_split =int(input("how many peoples to split the bill?        "))
    bill= round((total_bill + total_bill * (percentage_of_bill/100))/total_no_of_peoples_to_split)
    print(f"Each person should pay: ${bill}")

tip_calculator()

