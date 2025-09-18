# Write a function that divides two numbers.
def safe_divide(a,b):
    try:
        x = a/b
        return x
    except  ZeroDivisionError:
        return "Error"
print(safe_divide(10, 0))
print(safe_divide(10, 2))

# Ask the user to enter a number
while True:
    try:
        num = int(input("Enter a number: "))
        print("Thank You")

        break
    except ValueError:
        print("Invalid input! try again.")

# Try reading a file named data.txt
try:
    with open("data.txt", "w")as f:
        file = f.write("Hye!")
        print(file)
    with open("data.txt", "r")as f:
        file = f.read()
        print(file)
except FileNotFoundError:
    print("File not found")
finally:
    print("Operation Complete")

# Create a function that raise a value error if the number is negative.
def check_positive(num):
    try:
        if num > 0:
            print("Number must be positive")
    except ValueError:
        print("")
    
print(check_positive(10))
print(check_positive(-5))

# Write a program that write user input to output.txt.
try:
   text = input("Enter some text: ")
   with open("output.txt", "w")as f:
      f.write(text)
   with open("output.txt", "r") as f:
      read = f.read()
      print(read)
except IOError:
   print("Could not write to fail!")
finally:
   print("Writing complete")

# Write a program t oread 'log.txt' and append a new line.
try:
    with open("log.txt", "a") as f:
        text = "Welcome to our software house."
        write = f.write(text)
        print(write)
except FileNotFoundError:
    print("File not found. Creating new file...")

finally:
    print("Operation done")

# There is a bug in this function. Use print staments to find it:
def multiply_list(lst):
    result = 0
    for num in lst:
        result *= num
    return result
print(multiply_list(1, 2, 3, 4))

# convert user input to an integer
try:
    num = int(input("Enter a number: "))
    x = 100 / num
    print(x)
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# largest number
d = [34, 13, 45, 9, 23]
max_num = 0
for i in d:
 if i > max_num:
     max_num = i
print(max_num)

# Second largest no
b = [34, 13, 45, 9, 23]
max_num = 0
second_num = 0
for i in b:
    if i > second_num:
        second_num= i
        print(second_num)


# Swapping
a = 10
b = 15
print(a,b)
# c = a 
# a = b 
# b = c 
# print(a,b)

a = a + 5
b = b - 5
print(a,b)
 

       

