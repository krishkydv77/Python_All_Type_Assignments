# 1. Write a program to find the Greatest Common Divisor (GCD) of two
# numbers using a while loop.
# Input: 12 18
# Output: 6
# Input: 7 13
# Output: 1

#1.method 1:-
a= int(input("Enter number : "))
b= int(input("Enter number : "))
while b !=0:
    temp=b
    b= a%b
    a= temp
print("GCD : ",a)

#1.method 2:-
a= int(input("Enter number : "))
b= int(input("Enter number : "))
i=1
gcd=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        gcd=i
    i +=1
print("GCD : ",gcd)

#1. method 3:-
a= int(input("Enter number : "))
b= int(input("Enter number : "))
while b!=0:
    a,b=b,a%b
print("GCD : ",a)


#1. method 4.(my friend Rohan code):-
a = int(input("Enter a :"))
b = int(input("Enter b :"))
if a>b:
    max = a
else:
    max = b
i = max-1
while(i!=0):
    if a%i==0 and b%i==0:
        print(f"Grand Common Divisor of {a} abd {b} is :{i}")
        break
    i-=1
    


# 2. Check whether a number is a perfect number using a while loop. A perfect number is a positive integer that equals the sum of its proper
# positive divisors (all divisors excluding the number itself). For example, 6 is
# perfect because its proper divisors (1, 2, 3) add up to 6 (1 + 2 + 3 = 6)
# Input: 6
# Output: Perfect
# Input: 10
# Output: Not Perfect

n = int(input("Enter Number : "))
i=1
sum=0
while(i<n):
  if n%i==0:
    sum+=i
  i+=1
if(sum==n):
  print("Perfect")
else:
  print("Not Perfect")


# 3. Convert uppercase to lowercase and lowercase to uppercase using a
# while loop.
# Input: "HeLLo" Output: "hEllO"
# Input: "JAVA" Output: "java"

Enter =input("Enter string : ")
i=0
output =" "
while i<len(Enter):
    alp= Enter[i]
    if alp.islower():
        output += alp.upper()
    elif alp.isupper():
        output +=alp.lower()
    else:
        output +=alp
    i +=1 
print("output :",output)


# 4. Print pattern for n lines
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1

n=int(input("Enter number : "))
for row in range(1,n+1):
    for col in range(1,row+1):
        if(row+col)%2 !=0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

# 5. Hourglass Star Pattern

#   *   *   *   *
#     *   *   *
#       *   *
#         *
#       *   *
#     *   *   *
#   *   *   *   *

n=int(input("Enter Number : "))
for row in range(1,n):
    for i in range(1,row+1):
        print(" ",end=" ")
    for col in range(n,row,-1):
        print("*  ",end=" ")
    print()
for row in range(2,n):
    for i in range(n,row,-1):
        print(" ",end=" ")
    for col in range(1,row+1):
        print("*  ",end=" ")
    print() 

# 6. Zig-Zag Star Pattern

# *   *   * 
#   *   *   
# *   *   *

n= int(input("Enter Number : "))
for row in range(1,n-2):
    for col in range(1,n):
        if(row+col)%2==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()





