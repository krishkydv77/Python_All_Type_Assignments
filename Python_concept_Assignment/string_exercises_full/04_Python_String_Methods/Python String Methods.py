#1.Write a program to convert a string into uppercase using the upper() method.
var = input('Enter String :')
print(var.upper())

#2.Write a program to convert a string into lowercase using the lower() method.
var = input('Enter String :')
print(var.lower())

#3.Write a program to convert the first character of each word into capital using the title() method.
var = input('Enter String :')
print(var.title())

#4.Write a program to capitalize the first character of a string using the capitalize() method.
var = input('Enter String :')
print(var.capitalize())


#5. Write a program to remove the leading and trailing spaces from a string using strip().
myInput = input('Enter string :')
print(myInput)

print(myInput.strip())

#6. Write a program to remove spaces only from the left side using lstrip().
myInput = input('Enter string :')
print(myInput.lstrip())

#7. Write a program to remove spaces only from the right side using rstrip().
myInput = input('Enter string :')
print(myInput.rstrip)


#8. Write a program to split a sentence into words using split() and print each word separately.
mystring = input('Enter string : ')
print(mystring)
print(mystring.split(' '))
print(mystring.split('s')) # if sentance maltipule 's'

#9. Write a program to join a list of words using join() and form a string with spaces in between.
myInput = input('Ente string :')
joint = ' '.join(myInput)
print(joint)             


#10. Write a program to replace all spaces in a string with an underscore (_) using 
#replace(). 
myInput = input('Enter string :')
output = myInput.replace(" ","_")
print(output)


#11. Write a program to find the index of the first occurrence of "is" in the string "This is 
# Python" using find().
myInput =  "This is Python"
index = myInput.find("is")
print("the index of the first occurrence of",index)




#12. Write a program to count the number of times 'a' appears in a string using count().
word = 'appears' 
print(word.count('a'))


#13. Write a program to check if a string starts with "Hi" using startswith(). 
myInput = input('Enter string: ')
if myInput.startswith('hi'):
    print("start with hii")
else:
    print('other start')


#14. Write a program to check if an email ends with ".com" using endswith().
myInput = input('Enter string :')
if myInput.endswith('.com'):
    print('email end with .com')
else:
    print('email not valid')


#15. Write a program to check if a string contains only alphabets using isalpha().
myInput = input('Enter string :') 
if myInput.isalpha():
    print("Alphabet")
else:
    print("mix")



#16. Write a program to check if a string contains only digits using isdigit().
myInput = input('Enter string :') 
if myInput.isdigit():
    print("only digits")
else:
    print("mix")


#17. Write a program to check if a string contains only alphanumeric characters using isalnum().
myInput = input('Enter string :')                 # alphabet and numerical dono ho sakte hai.
if myInput.isalnum():
    print("alpha + num")
else:
    print("mix")   




#18. Write a program to check if the string contains only white spaces using isspace(). 
myInput = input('Enter string :')
#myInput = "  "
#myInput = "krishan     "
if myInput.isspace():
    print('myInput isspace')
else:
    print('not valid')





#19. Write a program to take a sentence from the user and convert the whole text into 
#title case, then count how many times the word "The" appears. 

myInput = "the use of technology has revolutionized the way we communicate"
convert_title = myInput.title()
print(convert_title)
print(convert_title.count("The"))