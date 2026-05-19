# Day 2 - Part 2: User input and f-strings

name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))
age = 2026 - birth_year
print(f"Hi {name}, you are {age} years old in 2026.")