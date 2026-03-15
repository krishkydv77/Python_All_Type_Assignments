# Exception handling mechanism through which we manege/handle those event.
'''
to handle this 2 block

1) try  : jis code ko chalana hai
2) except : vo block jisme uss event ko handle karte hai
'''

# try:
#     x=10
#     x=x+10
#     print("x :",x)
#     z=x+y  # error 
#     print("Hello")
#     print(x,z)
# except Exception as rohan:
#     print("we found an error",rohan)



# try:
#     x=10
#     x=x+10
#     print("x :",x)
#     try:
#         print("inside the nested try")
#         z=x+y  # error 
#     except:
#         print("Error found inside the nested except block")
#     print("Hello")
#     print(x,z)
# except Exception as rohan:
#     print("we found an error",rohan)



# try:
#     def calculate(n):
#         try: 
#              print("n value: ",n)
#              a=int(input("Enter number a: "))
#              print("value of a: ",a)
#         except:
#          print("value of a is incrroect")
#         print(n+2)


#     calculate(10) # here calling function
# except:
#     print("issue in finction declaration /calling")





try:
    with open("data.txtx","r") as f:
        print(f.read())
except Exception as e:
    print("erro aai: ",e)
finally:
    print("inside finally")
    with open("data.tatx","w") as f:
        f.write("jsjdkajkjahfkj")
