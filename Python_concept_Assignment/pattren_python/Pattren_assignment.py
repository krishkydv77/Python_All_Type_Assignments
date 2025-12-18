# * * * * * 
# *       *
# *       *
# *       *
# * * * * *
# n = int(input("Enter Number : "))
# for row in range(n):
#     for col in range(n):
#         if( row==0 or row==n-1 or col==0 or col==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()



#     * * * * 
#      * * * *
#       * * * *
#        * * * *
       
# n = int(input("Enter Number : "))
# for row in range(n):
#     for i in range(n+row):
#         print(" ",end= "")
#     for col in range(n):
#         print("*" ,end=" ")
#     print()



# A
# A B
# A B C
# A B C D
# A B C D E
# n = int(input("Enter Number : "))
# for row in range(n+1):
#     for col in range(row):
#         print(chr(65+col),end=" ")
#     print()





# A
# B B
# C C C
# D D D D
# E E E E E
# n = int(input("Enter Number : "))
# for row in range(n+1):
#     for col in range(row):
#         print(chr(64+row),end=" ")
#     print()



#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# n = int(input("Enter Number : ")) 
# for row in range(n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(row,0,-1):
#         print("*",end=" ")
#     print()


#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
# n = int(input("Enter Number : ")) 
# for row in range(n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     temp=1
#     for col in range(row,0,-1):
#         print(temp,end=" ")
#         temp +=1
#     print()


# 1 2 3 4 5 
#   1 2 3 4
#     1 2 3
#       1 2
#         1
# n =int(input("Enter Number : "))
# for row in range(n,0,-1):
#     for i in range(n-row):
#         print(" ",end=  " ")
#     temp =1
#     for col in range(row,0,-1):
#         print(temp,end=" ")
#         temp +=1
#     print()


# A B C D E 
#   A B C D
#     A B C
#       A B
#         A
# n =int(input("Enter Number : "))
# for row in range(n,0,-1):
#     for i in range(n-row):
#         print(" ",end=  " ")
#     temp =0
#     for col in range(row,0,-1):
#         print(chr(65+ temp),end=" ")
#         temp +=1
        
#     print()


#      * * * * *
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
# n = int(input("Enter Number : "))
# for row in range(n):
#     for i in range(n-row):
#         print(" ",end= "")
#     for col in range(n):
#         print("*" ,end=" ")
#     print()


#     1 2 3 4 5 
#    1 2 3 4 5
#   1 2 3 4 5
#  1 2 3 4 5
# 1 2 3 4 5
# n = int(input("Enter Number : "))
# for row in range(1,n+1):
#     for i in range(n-row):
#         print(" ",end= "")
#     for col in range(1,n+1):
#         print(col ,end=" ")
#     print()





#     A B C D E
#    A B C D E
#   A B C D E
#  A B C D E
# A B C D E
# n = int(input("Enter Number : "))
# for row in range(1,n+1):
#     for i in range(n-row):
#         print(" ",end= "")
#     temp =0
#     for col in range(1,n+1):
#         print(chr(65+temp) ,end=" ")
#         temp +=1
#     print() 


#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# method =1
# n= int(input("Enter Number : "))
# for row in range(n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(row,0,-1):
#         print("*",end=" ")
#     print()

    
# for row in range(n):
#     for col in range(row):
#         print("*",end=" ")
#     print()


# method =2
# n = int(input("Enter Number : "))

# for row in range(n):
#     for i in range(n-row-1):
#         print(" ", end=" ")
#     for col in range(2*row+1):
#         print("*", end=" ")
#     print()





#         * 
#       *   *
#     *       *
#   *           *
# * * * * * * * * *
# n= int(input("Enter Input : ") )
# for row in range(n):
#     for i in range(n-row):
#         print(" ", end=" ")
#     for col in range(2*row+1):
#         if(col==0 or col==2*row or row ==n-1):
#             print("*", end=" ") 
#         else:
#             print(" ",end=" ")
#     print()




# * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# n = int(input("Enter Number : "))

# for row in range(n,0,-1):
#     for i in range(n-row):
#         print(" ", end=" ")
#     for col in range(2*row-1):
#         print("*", end=" ")
#     print()



# *
# * *       
# * * *     
# * * * *   
# * * * * * 
# * * * *   
# * * *     
# * *       
# *
# n=int(input("Enter Number : "))
# for row in range(n+1):
#     for col in range(row):
#         print("*",end=" ")
#     print()
# for row in range(n):
#     for col in range(n-1,row,-1):
#         print("*",end=" ") 
#     print() 




#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# n=int(input("Enter Number : ")) 
# for row in range(n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(row,0,-1):
#         print("*",end=" ")
#     print()
# for row in range(n-1,0,-1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(row,0,-1):
#         print("*",end=" ")
#     print() 







#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# n = int(input("Enter Number : "))

# for row in range(n):
#     for i in range(n-row-1):
#         print(" ", end=" ")
#     for col in range(2*row+1):
#         print("*", end=" ")
#     print()
# for row in range(n-1,0,-1):
#     for i in range(n-row):
#         print(" ", end=" ")
#     for col in range(2*row-1):
#         print("*", end=" ")
#     print() 

# Half Pyramid
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=int(input("Enter number : "))
# for row in range(n+1):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()



# Hollow Half Pyramid
# 1
# 1 2
# 1   3
# 1     4
# 1 2 3 4 5


# n=int(input("Enter number : "))
# for row in range(n+1):
#     for col in range(1,row+1):
#         if(col==1 or col==row or row==n):
#             print(col,end=" ")
#         else:
#             print(" ",end=" ")
        
#     print()



# Inverted half Pyramid
# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# n=int(input("Enter number : ")) 
# for row in range(n+1):
#     temp =1
#     for col in range(n,row,-1):
#         print(temp,end=" ")
#         temp +=1
#     print()


# Inverted half Pyramid
# 5 4 3 2 1 
# 4     3   
# 3   2     
# 2 1       
# 1 

# n=int(input("Enter number : ")) 
# for row in range(n+1):
#     temp=5
#     for col in range(n,row,-1):
#         if(col==n or row ==0 or col==row+1):
#             print(temp-row,end=" ")
#             temp -=1
            
#         else:
#             print(" ",end=" ")
#     print()


# full prymid
#           1
#         1 2 3
#       1 2 3 4 5
#     1 2 3 4 5 6 7       
#   1 2 3 4 5 6 7 8 9     
# 1 2 3 4 5 6 7 8 9 10 11

# n = int(input("Enter Number : "))
# for row in range(n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         print(col+1,end=" ")
#     print()





#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9
#   1 2 3 4 5 6 7
#     1 2 3 4 5
#       1 2 3
#         1


# n = int(input("Enter Number : "))
# for row in range(n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         print(col+1,end=" ")
#     print() 
# for row in range(n-1,0,-1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         print(col+1,end=" ")
#     print()




# * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


# n= int(input("Enter Number : "))
# for row in range(n,0,-1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         print("*",end=" ")
#     print()
# for row in range(2,n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         print("*",end=" ")
#     print()





# A B C D E F G H I 
#   A B C D E F G   
#     A B C D E     
#       A B C       
#         A
#       A B C       
#     A B C D E     
#   A B C D E F G   
# A B C D E F G H I

# n= int(input("Enter Number : "))
# for row in range(n,0,-1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         print(chr(65+col),end=" ")
#     print()
# for row in range(2,n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         print(chr(65+col),end=" ")
#     print()




# * * * * * * 
# *         *
# *         *
# *         *
# *         *
# * * * * * *

# n= int(input("Enter Number : "))
# for row in range(n+1):
#     for col in range(n+1):
#         if(col==0 or row==0 or row==n or col==n):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()





# 1 2 3 4 5 
# 1       5
# 1       5
# 1       5
# 1 2 3 4 5

# n= int(input("Enter Number : "))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if(col==1 or row==1 or row==n or col==n):
#             print(col,end=" ")
#         else:
#             print(" ",end=" ")

#     print()



# A B C D E 
# A       E
# A       E
# A       E
# A B C D E

# n= int(input("Enter Number : "))
# for row in range(n):
#     for col in range(n):
#         if(col==0 or row==0 or row==n-1 or col==n-1):
#             print(chr(65+col),end=" ")
#         else:
#             print(" ",end=" ")

#     print()


#         *
#       *   *       
#     *       *     
#   *           *   
# *               * 
#   *           *   
#     *       *     
#       *   *       
#         *
# n= int(input("Enter Number : "))
# for row in range(n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         if(col==0 or col==2*row-2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()
# for row in range(n-1,0,-1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         if(col==0 or col==2*row-2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



#         A
#       A   C
#     A       E
#   A           G
# A               I
#   A           G
#     A       E
#       A   C
#         A
# n= int(input("Enter Number : "))
# for row in range(n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         if(col==0 or col==2*row-2):
#             print(chr(65+col),end=" ")
#         else:
#             print(" ",end=" ")    
#     print()
# for row in range(n-1,0,-1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(2*row-1):
#         if(col==0 or col==2*row-2):
#             print(chr(65+col),end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# * * * * 
# * * *
# * *
# *
# * *
# * * *
# * * * *

# n= int(input("Enter Number : "))
# for row in range(n):
#     for col in range(n,row,-1):
#         print("*",end=" ")
#     print()
# for row in range(2,n+1):
#     for col in range(row):
#         print("*",end=" ")
#     print()




# * * * * * 
#   * * * *
#     * * *
#       * *
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# n= int(input("Enter Number : "))
# for row in range(n,0,-1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(row,0,-1):
#         print("*",end=" ")
#     print()
# for row in range(2,n+1):
#     for i in range(n-row):
#         print(" ",end=" ")
#     for col in range(row,0,-1):
#         print("*",end=" ")
#     print()



# * * * * * * * * * * 
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *

# n=int(input("Enter Number : "))
# for row in range(n,0,-1):
#     for col in range(row):
#         print("*",end=" ")
#     for i in range(2*(n-row)):
#         print(" ",end=" ")
#     for col1 in range(row):
#         print("*",end=" ")
#     print()
# for row in range(2,n+1):
#     for col in range(row):
#         print("*",end=" ")
#     for i in range(2*(n-row)):
#         print(" ",end=" ")
#     for col1 in range(row):
#         print("*",end=" ")
#     print()




# *                 * 
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

# n=int(input("Enter Number : "))
# for row in range(1,n):
#     for col in range(row):
#         print("*",end=" ")
#     for i in range(2*(n-row)):
#         print(" ",end=" ")
#     for col in range(row):
#         print("*",end=" ")
#     print()
# for row in range(n,0,-1):
#     for col in range(row):
#         print("*",end=" ")
#     for i in range(2*(n-row)):
#         print(" ",end=" ")
#     for col in range(row):
#         print("*",end=" ")
#     print()



# n = int(input("Enter Number : "))
# for row in range(n):
#     for i in range(n-row):
#         print(" ",end= "")
#     for col in range(n):
#         if col==0 or row==n-1 or col ==n-1 or row ==0:
#             print("*",end=" ")
        
            
#     print()



n=4
temp=0

for row in range(1,n+1):
    temp +=1
    for i in range(n-row):
        print(" ",end=" ")
    for col in range(temp,temp+row):
        print(col,end=" ")
    kutta=2
    for col in range(row-1):
        print(kutta+0,end=" ")
        kutta +=1
        
    print()















    





















    



    
        
            
           
    




    








        
    
    

 




