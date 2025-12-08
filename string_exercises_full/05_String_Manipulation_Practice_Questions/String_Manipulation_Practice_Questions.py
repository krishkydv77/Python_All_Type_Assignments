# 1. Vowel-based Word Count
# Count how many words in a sentence start AND end with a vowel
# (case-insensitive).

sentence = input("Enter String : ")
vowel ="aeiouAEIOU"
words = sentence.split()
print(words)
count = 0
for c in words:
  if c[0] in vowel and c[-1] in vowel:
    count +=1
print(" start and end in vowel",count)




# 2. Palindrome Words
# Print all palindrome words found in a given sentence.
# ○ Example: "mom and dad went to civic center" -> output: mom dad civic


sentence = input("Enter String :")
words = sentence.split()
for c in words:
  if c[0]==c[-1]:
    
    print(c)
  # else:
    # print("not palindrome words")


# 4. Prime Digits Count
# Take a numeric string and count how many digits are prime (2, 3, 5, 7).

number = input("Enter string : ")
primeDigit ={'2', '3', '5', '7'}
count = 0
for c in number:
  if c in primeDigit:
    count +=1
print("prime digit : ",count)





# 5. Sum of Digits in Alphanumeric String
# Add only the digits from the input string.
# ○ Example: "a1b4c2" -> Output: 7

enterinput = input("Enter String : ")
sum =0
for c in enterinput:
  if c.isdigit():
    sum =sum +int(c)
print("sum digit :",sum)


# ○ Reverse String Without Slicing
enterinput = input("Enter String : ")
revers =""
for c in enterinput:
  revers = c + revers

print("reverse :",revers)

# Reverse a string using loops only.