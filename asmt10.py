name = input("Enter Customer Name: ")
slab = input("Enter Slab Type: ")
unit = int(input("Enter Units Consumed: "))
print("-------------------------------------------------------------------")
if slab == "industry" :
    print("Enter Customer Name: ",name)
    print("Enter Slab Type: ",slab)
    print("Enter Units Consumed: ",unit)
    print("Total Bill for usage: ",(unit*5.25))

elif slab == "commercial":
    print("Enter Customer Name: ",name)
    print("Enter Slab Type: ",slab)
    print("Enter Units Consumed: ",unit)
    print("Total Bill for usage: ",(unit*4.00))

elif slab == "residence":
    print("Enter Customer Name: ",name)
    print("Enter Slab Type: ",slab)
    print("Enter Units Consumed: ",unit)
    print("Total Bill for usage: ",(unit*3.08))
