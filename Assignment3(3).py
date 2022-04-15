eng = int(input("Enter your eng101 marks"))
math = int(input("Enter your mth101 marks"))
isl = int(input("Enter your isl202 marks"))
pak = int(input("Enter your pak301 marks"))
phy = int(input("Enter your phy101 marks"))
cs = int(input("Enter your cs101 marks"))

total = eng + math + isl + pak + phy + cs
per = total/600*100
print("your obtained number are:", total)
print("You got",per,"%")

if per >=90:
    print("you got 'A+' grade and your gpa is '4.00' ")

elif per>=85:
    print("you got 'A' grade and your gpa is '4.00' ")  

elif per>=80:
    print("you got 'A-' grade and your gpa is '3.99' ")

elif per>=75:
    print("you got 'B+' grade and your gpa is '3.65' ")

elif per>=71:
    print("you got 'B' grade and your gpa is '3.32' ") 

elif per>=68:
    print("you got 'B-' grade and your gpa is '2.99' ")

elif per>=61:
    print("you got 'C' grade and your gpa is '2.65' ")

elif per>=50:
    print("you got 'D' grade and your gpa is '1.99' ")
else:
    print("you got 'F' grade and you are 'Fail' ")                                     