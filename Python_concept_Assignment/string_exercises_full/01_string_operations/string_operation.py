String Operation
#Q1. Write a program to check if a string starts with the word "Hello".
myInput =input('Enter String : ')
if myInput.startswith("hello"):
    print("start with hello")
else:
    print("not start with hello")




#Q2.Check if the given string ends with ".com".
myInput =input('Enter String : ')
if myInput.endswith(".com"):
    print("valid email")
else:
    print("not valid")


#Q3.Write a program to check if "Python" starts with "Py" and ends with "on".
myInput = "Python"

myInput =input("Enter String: ")
if myInput.startswith("Py") and myInput.endswith("on"):
    print("start and end done")
else:
    print("try again")


#Q4.Take a string input and check if it contains only alphabets.
myInput = input("Enter string :")
if myInput.isalpha():
    print(myInput)
else:
    print("Try again")

#Q5. Check if a password contains both alphabets and digits using isalnum().
passw = input("Enter password")
if passw.isalnum():
    print("right password")
else:
    print("worng password")

#Q6. Check if an input string contains only digits using isdigit().
myInput = input("Enter string :")
if myInput.isdigit():
    print(myInput)
else:
    print("Try again")


#Q7. Write a program to check if a string contains only spaces using isspace().
sent = input("Enter String : ")
if sent.isspace():
    print("use space")
else:
    print("not use space")




#Q8 Ask the user to enter their name and validate that it is alphabetical.

name = input("Enter Name")
if name.isalpha():
    print(name)
else:
    print("name not valid")




#Q9. Check whether a vehicle number plate (input) contains both digits and alphabets.
vehicleNumber =input("vehicle Number: ")
if vehicleNumber.isalnum():
    print(vehicleNumber)
else:
    print("vehicle number not valid")



#Q10. Concatenate first name and last name and print the full name.
firstNanme =input("Enter name: ")
LastName = input("Enter last Name: ")
fullName = firstNanme +" " + LastName
print(fullName)


#Q11. Print a string 5 times using the * operator.
log = " Vande Mataram "
print(log*5 )


#Q12. Concatenate "Python" and "Programming" using the + operator.
firstP = "Python"
lastP = "Programming"
# chapter = firstP + " " + lastP
print(firstP + " " + lastP)


#Q13. Multiply the string "*" by a user input number.
multi =int(input("Enter multiply :"))
name ="krishan "
print(name * multi)


#Q14. Iterate through a string and print each character on a new line.
myInput = "krishan"
print("\n".join(myInput))

    according sir
for c in myInput:
    print(c)


#Q15. Count and print vowels by iterating through the string.
myInput =input('Enter string')
vowels ='aeiouAEIOU'
count=0
for c in myInput:
    if c in vowels:
        count +=1
print("count vowels",count)



#Q16. Print each character with its index number (string: "India").
myInput ="India"
for i in range(len(myInput)):
    print(i,myInput[i])





