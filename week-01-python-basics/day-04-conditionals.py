#voting eligibility
age_input = input("Enter your age:")
try:
    age=int(age_input)
except ValueError:
    print(f"Entered age is not valid. Please enter whole numbers like 18")
else:
    if age < 0 :
        print("Age can't be negative")
    elif age < 18 :
        print(f"You're {age}, wait {18 - age} more years to vote!")
    elif age<=100:
        print(f"You're {age}. You can vote.")
    else:
        print("That's suspicious age.")

#Grade Calculator
marks_input = input("Enter your marks b/w 0-100 : ")
try:
    marks = int(marks_input)
except ValueError:
    print(f"You entered wrong input.Please enter the correct value b/w 0-100.")
else:
    if marks < 0 or marks > 100:
        print(f"{marks} is out of range. Marks must be between 0 and 100.")
    else:
        if marks >=90:
            grade = "Grade A"
        elif marks >=75:
            grade = "Grade B"
        elif marks >= 60:
            grade = "Grade C"
        elif marks >=40:
            grade = "Grade D"
        else:
            grade = "Fail"
        
        print(f"Your grade is {grade}")


#Day Classifier
day = input("Enter any day : ").strip().lower()

if day in ["saturday","sunday"]:
    print("Weekend!")
elif day in ["monday","tuesday","wednesday","thursday","friday"]:
    print("Working day!")
else:
    print("Not a valid day!")


#Login simulator
username = input("\nUsername: ")
password = input("Password: ")

if username == "noori" and password == "secret123":
    print("Login success!")
else:
    print("Invalid username or password")
