def prime_checker(number):
    for i in range(2,int(number/2)):
        if number % i ==0:
            return print("It's not a prime number.")
    return print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
