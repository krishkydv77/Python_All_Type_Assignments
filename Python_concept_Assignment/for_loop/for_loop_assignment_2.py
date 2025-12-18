Basic Iteration and Output

#1. Print numbers from 1 to 10 using a for loop.
for i in range(1,11,1):
    print(i)
# 2. Print all even numbers between 1 to 50.

for j in range(1,51,1):
    if j%2==0:
        print(j)
#3. Print all odd numbers between 1 to 50.

for k in range(1,51):
    if k%2 !=0:
        print(k)
#4. Print numbers from 10 to 1 (reverse order).
for l in range(10,0,-1):
    print(l)





#Mathematical Operations
#1. Print the multiplication table of 5 (from 1 to 10).
for a in range(1,11):
    table = 5*a
    print(f"5*{a}= {table}")

#2. Take a number input and print its multiplication table up to 10.
digit = int(input("Enter number :"))
for i in range(1,11):
    print(f"{digit}*{i}={digit*i}")

#3. Print the sum of first 10 natural numbers.
sum =0
for j in range(1,11):
    sum +=j
print(sum)

#4. Take a number input $n$ and print the sum of numbers from 1 to $n$.
digit =int(input("Enter Number :"))
sum =0
for i in range(1,digit+1):
    sum +=i 
print(sum)

#5. Print squares of numbers from 1 to 10.
for i in range(1,11):
    squares = i*i
    print(f"{i}*{i} = {squares}")

#6. Print cube of each number from 1 to 10.
for i in range(1,11):
    cube = i**3
    print(f"{i} = {cube}")

#7. Print the factorial of a given number using a for loop.
digit = int(input("Entre number :"))
fect =1
for i in range(1,digit+1):
    fect *=i 
print(f"{digit} factorial= {fect}")

#8. Take 5 numbers from user and print their total sum.
digit = int(input("Entre number :"))
digit1 = int(input("Entre number :"))
digit2 = int(input("Entre number :"))
digit3 = int(input("Entre number :"))
digit4 = int(input("Entre number :"))
sum = digit + digit1 +digit2 +digit3 + digit4
print(f"total = {sum}")

#String and Digit Manipulation
#1. Print all characters of a string one by one in each line.
myInput = input("Enter string :")
for c in myInput:
    print(c)

#2. Count the number of vowels in a given string using a loop.

myInput = input("Enter string :")
vowels ="aeiouAEIOU"
count =0
for c in myInput:
    if c in vowels:
        count +=1
print(count)

# 3. Take a number input and count how many digits it has.
number =int(input("Enter Number : "))
count =0
for c in number :
    count +=1
print(count)

           sir wala samjao nhi ho rha hi.