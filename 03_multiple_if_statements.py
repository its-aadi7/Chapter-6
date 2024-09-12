a = int(input("Enter your age: "))

# If statement no: 1
if(a%2 ==0):
    print("a is even")
# End If statement no: 1

# If statement no: 2
if(a>=18):
    print("\033[1mYou are above the consent\033[0m")
    print("\003 \033[32mGood for you \033[0m \003")

elif(a<0):
    print("\033[1mYou are entering an invalid negative age\0330m")

elif(a==0):
    print("You are entering 0 Which is nat a valid age")

else:
    print("\033[1mYou are below the consent\033[0m")
# End If statement no: 2

print("End of Programme")