#1. Given a string "Hello World", print the first 5 characters using slicing.
name ='Hello World'
print(name[0:5])

#2. Write a program to input a string and print the string without the first and last character.
myName ='my name is krishan'
print(myName[1:-1])

#3. Slice the string "PythonProgramming" to get "Python" and "Programming" separately.
pro ='PythonProgramming'
print(pro[0:6])
print(pro[6:17])


#4. Given "apple", print the string in reverse using slicing. (Do not use reversed() or loop)
fruit ='apple'
print(fruit[::-1])



#5. Input a string and print only the characters at even indexes using slicing.
myInput = input('Enter string: ')
print(myInput[1::2])

#6. Input a string and print only the characters at odd indexes using slicing.
print(myInput[0::2])


#7. Given "LearningPython", slice "Python" using negative indexing only.
var ='LearningPython'
print(var[-6:])

#8. Input a string and print the first half and second half separately using slicing.
myInput = input('Enter string: ')
midNumber = len(myInput)//2
print(myInput[:midNumber])
print(myInput[midNumber:])


#9. Given the string "DataScience", print "Science" using slicing.
data = 'DataScience'
print(data[4:])


#11. Given "SlicingExamples", print every 2nd character using slicing (step = 2).
myInput ='SlicingExamples'
print(myInput[1::2])


#12. Input a string and print the string after skipping the first 3 and last 3 characters.
myInput = input('Enter string: ')
if len(myInput) >=6:
    print(myInput[3:-3])
else:
    print('short string')


#13. From "abcdefghijklmnop", extract "ghijk" using slicing.
var = "abcdefghijklmnop"
print(var[6:-5])


#14. Input a string and print last 4 characters using slicing.
var = input('Enter string: ')
if len(var)>=5:
    print(var[-4:])
else:
    print('short string')



#15. Given "OpenAIChatGPT", display sliced formats:
# ○ a. 0 to 7
# ○ b. 4 to 10
# ○ c. Whole string in reverse.

hii = "OpenAIChatGPT"
print(hii[0:7])
print(hii[4:10])
print(hii[::-1])



#16. Input a string and print characters from index 2 to index len(string)-2 (exclude first and last 2).
hey = input('Enter input :')
if len(hey) >4:
    print(hey[2:-2])
else:
    print('short string')


#17. Given "ABCDEFG", print "ACEG" using slicing.
hii = 'ABCDEFG'
print(hii[0::2])


18. Input a string and print if the reverse of the string is the same - using slicing (Palindrome Check).
myInput =input('Enter input')
reverse = myInput[::-1]
if myInput==reverse:
    print('Palindrome')
else:
    print('not palindrome')



#19. Given "HelloPython", extract "loPy" using slicing.
hello = 'HelloPython'
print(hello[3:-4])

20. Input a string and print each character twice using slicing step logic only.
hii =input('input a string')
# double = ""
# double = hii*2
# print(double)

for c in hii:
    print(c*2,end=" ")






