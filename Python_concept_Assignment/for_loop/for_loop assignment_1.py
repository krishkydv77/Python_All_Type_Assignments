# #1. Print all even numbers from 1 to 50 using a for loop.

for i in range(1,51):
    if i%2==0:
        print(i)

# # 2. Print numbers from 1 to 100 but stop the loop if the number is 37. (Use break)

for i in range(1,101):    #loop stop 37
    print(i)
    if i==37:
        break
 #method 2 (but)
for i in range(1,101):    #loop stop 36
    if i==37:
        break 
    print(i)
    

# # 3. Print numbers 1 to 50 but skip multiples of 5. (Use continue)

for i in range(1,51):
    if i==5:
        continue 
    print(i)
    
    
# # 4. Take a number from the user and print its multiplication table (1–10).

number = int(input("Enter number :"))
for i in range(1,11):
    print(f"{number}*{i}={number*i}")

# # 5. Count how many numbers between 1 to 100 are divisible by 7.

count =0
for i in range(1,101):
    if i%7==0:
        count +=1 
       # print(i)    # digit find divisible 7
print("count =",count)


# # 6. Print only the vowels from a string given by the user.

myInput = input("Enter string :")
vowels = "aeiouAEIOU"
for c in myInput:
    if c in vowels:
        print(c)

# # 7. Given a string, print the first 5 characters only and stop. (Use break)

myInput = input("Enter string :")
count =0
for c in myInput:
    print(c,end="")    #end="" -> means without new line
    count +=1
    if count ==5:
        break


# # 8. From numbers 1 to 20, skip odd numbers and print only squares of even numbers.

for i in range(1,21):
    if i%2==0:
        print(i**2)


# # 9. Take 10 numbers from the user and print the highest number.

n=0
li =[]
while n<=10:
    user_input =int(input("Enter a number : "))
    li.append(user_input)
    n +=1
print(max(li))
    


# # 10. Print all characters of a string except spaces. (Use continue)

myInput = input("Enter String : ")
for c in myInput:
    if c == " ":
        continue
    print(c,end="")

# # 11. Print the sum of all numbers from 1–100 but skip numbers divisible by 3.

sum =0
for i in range(1,101):
    if i%3 ==0:
        continue 
    sum +=i
print("sum =",sum)

# # 12. Given a list of numbers, stop printing when the number 0 is found. (Use break)
# # ○ Example: [3, 4, 1, 0, 7, 9] → stop at 0


# # 13. Check if a given number is prime or not using a for loop. 

number = int(input("Enter Number : "))
is_prime =True
if number > 1:
    for i in range(2,number):
        if number%i==0:
            is_prime = False
    if is_prime:
        print("prime number")
    else:
        print("Not prime number")
else:
    print("Please enter value >1")



# # 14. Print the factorial of a number using a for loop.
# # ○ Example: 5 → 120

fect =1
number = int(input("Enter String :"))
for i in range(1,number+1):
    fect *=i 
print("fectorial = ",fect)

# # 15. Print the smallest number in a list.

# # 16. Count how many vowels are in the string: "Hello Python Programmer"

stri = "Hello Pyhton Programmer"
vowels ="aeiouAEIOU"
count = 0
for c in stri:
    if c in vowels:
        count +=1       
print("total vowel = ",count)

# # 17. Print numbers 1–30; if a number is divisible by both 4 and 6, then stop. (Use break)

for i in range(1,31):
    print(i)
    if i%4==0 and i%6==0:
        break
    
# # 18. Print only negative numbers from a given list.

# # 19. Reverse a string using a for loop.
# # ○ Example: "python" → "nohtyp"



# # 20. Print the Fibonacci series up to N terms using a for loop.
a=0
b=1
num = int(input("Enter number : "))
for i in range(num):
    print(a)
    a,b = b,a+b