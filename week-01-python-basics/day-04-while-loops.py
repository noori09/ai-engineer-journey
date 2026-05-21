# 1. Basic countdown
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# 2. Input validation — keep asking until valid age
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        if age < 0:
            print("Age can't be negative")
            continue    # skip and re-ask
        break    # valid — exit loop
    except ValueError: 
        print(f"{age_input} is not a number.Try again")

print(f"You are {age} years old")

# 3. Number guessing game
import random
secret = random.randint(1,10)
attempts = 0
print("\n Number Guessing Game ")
print("\n I am thinking of a number b/w 1 to 10")

while True:
    guess_input = input("Enter your guess: ")
    try: 
        guess = int(guess_input)
    except ValueError: 
        print("Please enter a valid input")
        continue
    
    attempts += 1
    if guess == secret:
        print(f"Correct! You got in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# break is mandatory in while True, if there's no break, the loop runs forever.

# 4. Print odd numbers from 1 to 20 using while + continue
count = 0
while count < 20:
    count +=1
    if count %2 == 0:
        continue
    print(f"{count}")
    