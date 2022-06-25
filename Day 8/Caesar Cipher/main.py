from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      new_position=new_position % len(alphabet)
      end_text += alphabet[new_position]
    else:
      end_text+=char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


x=True
while x == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart=input("Type 'yes' if you want to go again. Otherwise type 'no':\n   ").lower()
  if restart=="no":
    x=False
    print("Goodbye")



# For encryption
# def encrypt(plain_text,shift_no):
  
#   cipher_text=""
#   for i in text:
#     position = alphabet.index(i)
    
#     new_position=position+shift
#     new_position=new_position % len(alphabet)
#     new_letter=alphabet[new_position]
#     cipher_text+=new_letter
#   print(cipher_text)



# Decryption

# def decrypt(cipher_text,shift_no):
#   plain_text=""
#   for i in cipher_text:
#     position = alphabet.index(i)
#     new_position=position-shift
#     new_position=new_position % len(alphabet)
#     new_letter=alphabet[new_position]
#     plain_text+=new_letter
#   print(plain_text)

# if direction=="encode":
#   encrypt(plain_text=text,shift_no=shift)
# elif direction=="decode":
#   decrypt(cipher_text=text,shift_no=shift)


