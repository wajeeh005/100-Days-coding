
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list=[]
for i in range(nr_letters):
    pswd_letter= random.choices(letters)
    password_list.append(pswd_letter)
for i in range(nr_symbols):
    pswd_symbols= random.choices(symbols)
    password_list.append(pswd_symbols)

for i in range(nr_numbers):
    pswd_numbers= random.choices(numbers)
    password_list.append(pswd_numbers)



k=0


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
final=""
for i in range(len(password_list)) :
        final+=str(password_list[i][k])




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
        

#Method:1
# we can use random.shaffle to generate randomly from a list
final_shuffle= random.shuffle(password_list)
final2=""
for i in final_shuffle:
    final2+=i


#Method 2
final3=""
for i in range(len(password_list)) :
        indexx=random.randint(0,len(password_list)-1)
        final3+=str(password_list[indexx][k])
        password_list.remove(password_list[indexx])

print(final," Its Answer in Order first Letters then numbers and then symbols.")
print(final2," Its answer is in unorder and use of built in function suffle. ")
print(final3," Its answer is in unorder. ")