# file handling:-
# - data store
# -  peramanent
# - mechanism to handle file to read or write content

# -  1. open

#     2. read/write
#     3. close


f= open('krish.txt')
#print(f.read()) # file padne ke liye if file read mode open kiya ha to write nhi kar sakte

print(f)  # memeory address dega
f.close()

#k=open('')



f=open("krish.txt","w")
f.write("krishan kumar yadav and rohan") #write karte ha old content hatt jata ha or naya wala aa jata hai.
f.close()


#read or write dono karne ke liye "r+" use karte hai overwrite hota hai
f=open("krish.txt","r+")  #"w+" me ye write karne par phale ka complet data hata deta hai
f.write("rrrrr")  # mera deta ab 5th position se read hoga bcoz 5th tak rrrrr write hoga
out=f.read()
#f.write("kesav and ankit both engineer")
f.close()
print("file content: ",out)




# cursor ki postion
f=open("krish.txt","w+")
print("cursor 1:",f.tell())

out =f.read()
print("cursor 2 after read:",f.tell())
f.write("ind")  # write ke baad hi cursor ki postion badalti hai
print("cursor 3 postion:",f.tell())

# change postion
f.seek(10)   # jaha cursor ko leke jana le ja sakte hai
print("cusor 4th:",f.tell())
out=f.read()

f.close()
print("file content: ",out)


