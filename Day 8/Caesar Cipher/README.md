# Write a Caesar cipher program which encrypt and decrypt the message according to user demand.


### Following Steps You Should Follow
1.  Import and print the logo from art.py when the program starts.



2.  Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
3.  Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    ##### Example 
        plain_text = "hello"
        shift = 5
        cipher_text = "mjqqt"
        print output: "The encoded text is mjqqt"


4.  Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
5.  Inside the 'decrypt' function, shift each letter of the 'text' backwards in the alphabet by the shift amount and print the decrypted text.  
    ##### Example 
        cipher_text = "mjqqt"
        shift = 5
        plain_text = "hello"
        print output: "The decoded text is hello"


6. What happens if the user enters a number/symbol/space?
    Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    e.g. start_text = "meet me at 3"
    end_text = "•••• •• •• 3"


7. What if the user enters a shift that is greater than the number of letters in the alphabet?

##### **HINT**: Think about how you can use the modulus (%).

8.  Type 'yes' if you want to go again. Otherwise type 'no'.
      If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
##### **Hint:** Try creating a while loop that continues to execute the program if the user types 'yes'. 

