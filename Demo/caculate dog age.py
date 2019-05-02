# caculate dog age
age = int(input("please input your dog age: "))
if age < 0:
    print("You must be kidding!")
elif age == 1:
    print("equals to a 14-year-old teen")
elif age == 2:
    print("equals to a 22-year-old adult")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("equals to adult age: ", human)
## exit notification
input("please exit by pressing Enter")