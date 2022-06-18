#METHOD 1
def love_calculator1():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    combine_name=name1+name2
    name_in_lower_letter=combine_name.lower()
    truee=["t","r","u","e"]
    love=["l","o","v","e"]

    count1=0
    count2=0

    for i in truee:
        count1+=name_in_lower_letter.count(i)
    for i in love:
        count2+=name_in_lower_letter.count(i)
    love_score=int(str(count1)+str(count2))

    if love_score<10 or love_score>90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif love_score>40 and love_score<50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")

love_calculator1()
print("-------------------------------------------")
# METHOD 2
def love_calculator2():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")

    true="TRUEtrue"
    love="LOVElove"

    name=name1+name2
    sum1=0
    sum2=0
    for i in name:
        if i in true:
            sum1+=1
        if i in love:
            sum2+=1
    love_score=int(str(sum1)+str(sum2))


    if love_score<10 or love_score>90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif love_score>40 and love_score<50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")


#love_calculator2()