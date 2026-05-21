# The problem:
# Print numbers from 1 to 100, with these rules:

# If divisible by 3 → print "Fizz" instead of the number
# If divisible by 5 → print "Buzz" instead of the number
# If divisible by BOTH 3 AND 5 → print "FizzBuzz" instead of the number
# Otherwise → print the number itself

for i in range(1,101):
    if i%3 == 0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)