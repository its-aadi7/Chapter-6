a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))
d = int(input("Enter the number 4: "))

if(a>b and a>c and a>d):
    print("Greater number is a", a)

elif(b>a and b>c and b>d):
    print("Greater number is b", b)

elif(c>a and c>b and c>d):
    print("Greater number is c", c)

else:
    print("Greater number is d", d)