tm = int(input("Enter Your Total Marks Here: "))
if tm>360:
    print("You Have Passed This Examination in First Class")
elif tm>=300 and tm<360:
    print("You Have Passed This Examination in Second Class")
else:
    print("You Have Passed This Examination in Third Class")