# 1. Write to a file
file = open("hello.txt","w")
file.write("Hello World!")
file.close()

# write to a file proper way
#What if your code crashes between open() and close()? The file stays open. Stays half-written. Bad.
#To solve this, Python has a special pattern called the with statement. It auto-closes the file even if errors happen

with open("hello.txt","w") as file:
    file.write("Hello Noori!")
    file.write("\nSecond line")
    


#2. Read from a file

with open("hello.txt","r") as file:
    content = file.read()
    print(content)
    
#3. Append into a file

with open("hello.txt","a") as file:
    file.write("\nThird line")
    file.write("\nFourth line")
    
#4. Read line by line

with open("hello.txt","r") as file:
    for line in file:
        print(line)

# Notice the output has double-spacing? That's because each line in the file already ends with \n, and print() adds another \n. To fix
# .strip() removes whitespace (including newlines) from both ends of a string.

with open("hello.txt","r") as file:
    for line in file:
        print(line.strip())
        
        
# handling err in case file not found while read
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File doesn't exist yet.")