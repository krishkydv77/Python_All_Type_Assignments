with open("krish.txt","r") as f:
    print(f.read())


#line by line read ke liye loop ka use karege
with open("krish.txt","r") as f:
    for a in f:
        print("line:",a)


#without loop use
with open("krish.txt","r") as f:
    print(f.readline())
    print(f.readline())
print(f.readline())  # with ke bahar ye nhi chalega


#every line ek list me lene ke liye
with open("krish.txt","r") as f:
    print(f.readlines())   # list me data deta hai


with open("krish.txt","r") as f:
    var=f.readlines()
    for line in var:
        print(line.strip()) # extra space ko hatane ke liye .strip() use karege
    
    
