print("Task 1")
print("Enter the first list of the numbers:")
list1=input().split()
print("Enter the second list of the numbers:")
list2=input().split()
def uncommon(list1,list2):
    uncommon=[]
    for item in list1:
        if item not in list2:
            uncommon.append(item)
    for item in list2:
        if item not in list1:
            uncommon.append(item)
    return uncommon
uncommonlist=uncommon(list1,list2)
print(uncommonlist," is the list of the items that are uncommon in the lists")
print("Task 2")
print("Enter a number")
n=int(input())
for i in range(1,n):
    print(i*i)
print("Task 3")
print("Enter a text")
txt=input()
def insert_underscore(txt):
    vowels = "aeiouAEIOU"  
    result = []
    count = 0   
    i = 0
    while i < len(txt):
        result.append(txt[i]) 
        count += 1
        if count % 3 == 0 and i != len(txt) - 1:
            if txt[i] in vowels:
                if i + 1 < len(txt):
                    result.append(txt[i + 1])
                    i += 1 
                if i != len(txt) - 1:
                    result.append('_')
            elif i + 1 < len(txt) and txt[i + 1] == '_':
                continue 
            else:
                result.append('_')

        i += 1

    return ''.join(result)
result = insert_underscore(txt)
print(result)
print("Task 4")
import random

def number_guessing_game():
    while True:
        secret_number = random.randint(1, 100)
        attempts = 10
        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100. You have 10 attempts to guess it.")
        while attempts > 0:
            print(f"\nAttempts left: {attempts}")
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("You guessed it right!")
                break
            attempts -= 1
        if attempts == 0:
            print(f"\nYou lost. The correct number was {secret_number}.")
        play_again = input("Want to play again? (Y/Yes/OK): ").strip().lower()
        if play_again not in ['y', 'yes', 'ok']:
            print("Thanks for playing! Goodbye!")
            break
number_guessing_game()
print("Task 5")
def password_checker():
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Password is too short.")
        return
    has_uppercase = any(char.isupper() for char in password)
    if not has_uppercase:
        print("Password must contain an uppercase letter.")
        return
    print("Password is strong.")
password_checker()
print("Task 6")
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def print_primes():
    print("Prime numbers between 1 and 100:")
    for num in range(1, 101):
        if is_prime(num):
            print(num, end=" ")
print_primes()