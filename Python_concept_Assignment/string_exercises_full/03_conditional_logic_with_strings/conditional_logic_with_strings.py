#Q1. Check if a string starts with "A". If yes, print "Starts with A", else print "No".
myInput = input("Enter String :")
if myInput.startswith('A'):
    print("start with A")
else:
    print("NO")


#Q2. Take a string input and check whether its length is greater than 5.

myInput = input("Enter String : ")
if len(myInput)>5:
    print("input length greater 5")
else:
    print("less then 5")

#Q3. Ask the user to enter an email, then check if it ends with "@gmail.com".

email = input("Enter your emial : ")
if email.endswith("@gmail.com"):
    print("valid mail")
else:
    print("try again")

#Q4. Check if a string contains the letter 'a'. If present, print "Found".

myInput = input("Enter string : ")
if 'a' in myInput:
    print("Found")
else:
    print('not found')

#Q5. Write a program: If the string is entirely in uppercase, print "UPPERCASE", else print "Not uppercase".
myInput = input("Enter String :")
if myInput.isupper():
    print("UPPERCASE")
else:
    print("NOT UPPERCASE")

#Q6. Check if the first and last characters of a string are the same.
myInput = input("Enter String :")
if myInput[0] == myInput[-1]:
    print("same-same")
else:
    print("start != end")



#Q7.Input a username and check:
#    ○ If it contains a space → print "Invalid username"

#    ○ Else → print "Valid username"

username = input("Enter Username : ")
if " " in username:
    print("invalid username")
else:
    print("valid username")


# Q8. Ask the user to enter a password:
# ○ If length < 8: print "Weak Password"
# ○ Else print "Strong Password"

password = input("Enter password : ")
if len(password)< 8:
    print("Week password")
else:
    print("Strong password")


# Q9. Write a program to classify the string:
# ○ Only alphabets → "Alphabetic"
# ○ Only digits → "Numeric"
# ○ Alphanumeric (mix of both) → "Alphanumeric"


stringName = input("Enter string")
if stringName.isalpha():
  print("Alphabetic")
elif stringName.isdigit():
  print("Numeric")
elif stringName.isalnum():
  print("mix string")
else:
  print("other character")

#Q10. If a string ends with ".jpg" print "Image file", else print "Not image file".

image = input("Image name : ")
if image.endswith(".jpg"):
    print("Image")
else:
    print("Not Image")


#Q11. Take a sentence and check if it contains the word "India".

sent = input("Enter Sentence :")
if "India" in sent:
    print("india word found")
else:
    print("not india")


# Q12. Ask for a number (string input). If it is a digit, convert it to an integer and print the square of the number.

number = input("Enter String : ")
if number.isdigit():
    num =int(number)
    print("number Square :",num **2)
    print("number Square :",num * num)
else:
    print("invalid")



# Q13. Write a program to check:
# ○ If the string contains '@' → "May be an Email"
# ○ Else → "Not an Email"

email =input("Enter mail : ")
if "@" in email:
    print("May be an email")
else:
    print("not email")


# Q14. If a string contains spaces → print "Sentence"
# ○ Else → print "Single Word"

sent = input("Enter srting : ")
if " " in sent:
    print("Sentence")
else:
    print("Single word")


# Q15. Take a string and check:
# ○ If the length is even → print "Even Length"
# ○ Else → print "Odd Length"

sent = input("Enter srting : ")
if len(sent)%2==0:
    print("Even length")
else:
    print("odd length")

