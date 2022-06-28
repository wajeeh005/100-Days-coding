from art import logo
print(logo)

bid_dic={}
x = True

def highest_bid(bid_dictionary):
  highest_bid_value=0
  winner=""
  for i in bid_dictionary:
    amount=bid_dictionary[i]
    if highest_bid_value < amount:
      highest_bid_value=amount
      winner=i
  print(f"{winner} is the winner with the highest bid of {highest_bid_value}$.")
  
  
while x:
  name = input("Enter your name:  ")
  bid_price = int(input("Enter your bid prize: $ "))
  bid_dic[name]= bid_price
  for_countinue=input("Are there any other bidders? Type 'yes or 'no':    ").lower()
  if for_countinue=="no":
    x=False
    highest_bid(bid_dic)

