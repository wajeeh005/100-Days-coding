# Tip calcultor
#1. First greeting
# 2.  What was the total bill? ask from User
# 3.  What percentage tip would you like to give?
# 4.  give 3 options 10,12 or 15 
#         user can put any one of them 
# 5.  Ask How many people to split the bill?
# 6.  divide the whole bill on given n


print("Hello Welcome to Tip calculator")
total_bill =int(input("What is your total bill?"))
percentage_of_bill= input("Wat percentage you like? 10,12 or 15")
total_no_of_peoples_to_split =int(input("how many peoples to split the bill?"))
bill= (total_bill * (percentage_of_bill/100))/total_no_of_peoples_to_split