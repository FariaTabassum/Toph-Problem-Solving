Y = int(input())
if (Y % 400 == 0) :
    print("Yes")
elif (Y % 4 == 0) and (Y % 100 !=0) :
    print("Yes")
else:
    print("No")