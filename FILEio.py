# f = open("poems.txt","r")
# text = f.read()
# print(text)
# f.close()

# f = open("greeting.txt" , "a")
# f.write("Have a nice day\n")
# f.close()

# with open('greeting.txt','r') as f :
#     a = f.read()
# with open('greeting.txt','w') as f :
#     a = f.write("me")
# with open('greeting.txt','a') as f :
#     a = f.write("hello !")
# print(a)

with open("poems.txt", "r") as f:
    a = f.read()
print(a)

f = open("copy_poems.txt" , "w")
f.write(a)
f.close()

