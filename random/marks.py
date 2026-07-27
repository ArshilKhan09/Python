marks = int(input("marks:"))

if(marks>=85):
    print("PASS :Grade A")

elif(marks>=70 and marks<85):
    print("PASS :Grade B")

elif(marks>=50 and marks<70):
    print("PASS :Grade C")

elif(marks>=35 and marks<50):
    print("PASS :Grade D")

else:
    print("Fail")
