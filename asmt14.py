def sleep(a,b):
    if a == False and b == False:
        print(True)
    elif a== False and b== True:
        print(True)
    else:
        print(False)
a = bool(input("Enter True if it is a Weekday: "))
b = bool(input("Enter True if you are in Vacation: "))

sleep(a,b)
