a = int(input("Enter your age: "))

if(a>18):
    print("\033[1mYes, you are greater than 18\033[0m")
    print("\003 \033[32mGood for you. More oppertunity \033[0m \003")

elif(a==18):
    print("You are 18")

else:
    print("\033[1mYou are lesser than 18\033[0m")
    print("\033[31mIt's not good for you. less oppertunity \033[0m")

print("End of Programme")