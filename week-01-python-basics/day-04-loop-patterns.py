# 1. Print multiplication table for any number
num_input = input("Enter your number: ")
try:
    num = int(num_input)
except ValueError:
    print("Please enter valid number")
else:
    if num <= 0:
        print("Please enter a positive number")
    else:
        for i in range(1,11):
            print(f"{num} x {i} = {num*i}")

# 2. Sum of all numbers from 1 to 100
sum = 0
for i in range(1,101):
    sum += i 
print(f"{sum}")

# 3. Numbered list of friends
print("My friends: ")
friends = ["aman", "priya", "rahul", "sneha", "vikram"]
for index, friend in enumerate(friends,start=1):
    print(f" {index}. {friend.capitalize()}")

# 4. Find longest name
friends = ["aman", "priya", "rahul", "sneha", "vikram"]
longest_name = ""
for friend in friends:
    if len(friend) > len(longest_name):
        longest_name = friend
print(f"Longest name is : {longest_name}")


# 4.2 find longest and shortest name using min and max
friends = ["aman", "priya", "rahul", "sneha", "vikram"]
longest = max(friends,key=len)
shortest = min(friends,key=len)
print(f"longest name is : {longest} and shortest name is : {shortest}")


#5. Count vowels in word
name = input("Enter any name: ")
count = 0
for i in name:
    if i in "aeiou":
        count +=1
print(f"{name} has {count} vowels")