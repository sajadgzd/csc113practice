# SAJAD_GHOLAMZADEHRIZI
# SESSION AFTERNOON 1 _ InclassAssignment3
def collatz(n):
    try:
        n = int(n)
    except ValueError:
        print("Try to type a valid integer!")
    else:
        if n < 0:
            print("It was a negative integer, try to enter a positive integer!")
        elif n < 2:
            print("Try to enter an integer greater than 1. It should be at least 2!")
        else:
            if n % 2 ==0:
                newN = n//2
                print(newN)
                if newN != 1:
                    collatz(newN)
                #else:
                    #return (newN)
            elif n % 2 != 0:
                newN = 3 * n + 1
                print (newN)
                collatz(newN)

n = input("Enter an integer which is greater than 1 and not equal to 1 ( > 1)? \n")
collatz(n);

try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    print(a/b)
except ValueError:
    print("Please enter valid integers")
except ZeroDivisionError:
    print("The second number you entered was Zero, a number cannot be divided by Zero,\nplease try to enter a non zero number for that. ")
except:
    print("\nSomething went wrong, sorry!")


def primeFactors(num):
    print("Factors are:")
    i = 1
    while(i <= num): #while loop
        k = 0
        if(num % i == 0): #condition to check whether the number is prime or not
            j = 1
            while(j <= i): #logic for prime factor
                if(i % j == 0):
                    k = k + 1
                j = j + 1
            if(k == 2):
                print(i) #prints the prime factors
        i = i + 1

num = int(input("Enter an integer to get its prime factors? \n"))
primeFactors(num)


def pFact(x):
    if x < 3:
        print(2)
    elif x % x - 1 != 0:
        print(x)
        pFact(x - 1)
    else:
        pFact(x - 1)

x = int(input("Enter an integer to get the prime numbers which are less than or equal to it? \n"))
pFact(x)

print(2);
