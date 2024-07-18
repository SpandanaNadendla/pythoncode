a=int(input("no of classes held:"))
b=int(input("no of classes attented:"))
c=int((b/a)*100)
print("Attendance Percentage",c)
if (c>75):
    print("Student is allowed to sit in Exam")
else :
    print("Student is not allowed to sit in Exam")