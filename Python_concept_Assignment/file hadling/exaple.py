def primeCheck(n):
    count=0
    for i in range(2,n//2+1):
        if n%i==0:
            count+=1
        if count==2:
            print("prime number",n)
        else:
            print("not prime number:",n)



def file_read(filename):
    with open(filename,"r") as f:
        print("inside func")
        #line by line reading file content
        for line in f:
            print(line.strip(),type(line.strip()))
            print(int(line.strip()),type(int(line.strip())))
        #print(f.read())
            n=int(line.strip())
            primeCheck(n)

file_read("ex1.txt")




