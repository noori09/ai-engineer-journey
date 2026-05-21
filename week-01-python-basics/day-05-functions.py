# 1. Simplest function

def greet():
    print("hello")

greet()
greet()

# 2. A function that does multiple things

def show_menu():
    print("\n ====== Main Menu ======")
    print("1. Start game")
    print("2. View scores")
    print("3. Quit")

show_menu()
print("(some other code here)")
show_menu()

# 3. A function with a clear, named purpose
def print_separator():
    print("-" * 40)

print("Top Section")
print_separator()
print("Bottom Section")



# Parameters
def greet(name):
    print(f"Hello {name}")

greet("noori")
greet("ekta")


# Multiple parameters

def add(a,b):
    print(f"{a} + {b} = {a+b}")

add(3,5)
add(2,2)

#Return values
def square(x):
    return x*x

result = square(4)
print(f"Square of 4 is {result}")
print(f"Square of 5 is : {square(5)}")

# --- Boolean returns (validation pattern) ---
def is_adult(age):
    return age>=18
print(is_adult(28))
print(is_adult(15))
if is_adult(19):
    print("Can vote")
    
def is_valid_phone(phone):
    return len(phone) == 10 and phone.isdigit()

print("Is Valid Phone")
print(is_valid_phone("9878552499"))
print(is_valid_phone("333"))

#Guard close pattern
def can_drive(age,has_license):
    if age < 18:
        return False
    elif not has_license:
        return False
    else:
       return True
print("Can drive")
print(can_drive(17,True))
print(can_drive(18,False))
print(can_drive(19,True))



#Celsius to Fahrenheit
def celsius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

print("Celsius to Fahrenheit")
print(celsius_to_fahrenheit(0))     
print(celsius_to_fahrenheit(100))    
print(celsius_to_fahrenheit(37)) 

# is even
def is_even(num):
    return num % 2 == 0 

print("Is Even")
print(is_even(4))    
print(is_even(7))

#Longest word
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print("Longest word")
print(longest_word(["cat", "elephant", "dog"]))   
print(longest_word(["a", "bb", "ccc"]))        


# 1. Local vs global
name = "noori"

def show_name():
    print(f"Hello {name} from inside")

show_name()
print(f"Hello {name} from outside")

# --- 2. Local variable, isolated from global ---
count = 100

def use_count():
    count = 5
    print(f"count inside is {count}")

use_count()
print(f"count outside is {count}")

# --- 3. Function modifies a list (mutation, not reassignment) ---

scores = []

def add_score(s):
    scores.append(s)

add_score(4)
add_score(10)
add_score(44)
print(f"scores {scores}")

# --- 4. Parameters are local ---
def greet(person):
    person = person.upper()
    print(f"Hello {person}")

my_name = "noori"
greet(my_name)
print(f"my name after greet {my_name}")


# --- 5. The "forgot to return" trap ---
def double(num):
    num = num*2
result = double(5)
print("result", result)


# --- 6. Fixed version ---

def double_correct(x):
    return x * 2

result = double_correct(5)
print("Correct result:", result)    # 10