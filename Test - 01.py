Eggs=int(input("Total number of eggs? "))
Boxes12=Eggs//12
Boxes6=(Eggs-Boxes12*12)//6
print("Boxes of 12: ",Boxes12)
print("Boxes of 6: ",Boxes6)
if Boxes12*12+Boxes6*6==Eggs:
    print("No loose eggs")
else:
    print("Loose eggs: ",Eggs-Boxes12*12-Boxes6*6)