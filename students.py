#!/usr/bin/env python3
n = int(input("please enter the number of students: "))
data = {}    #字典
subjects = ('Physics', 'Maths', 'History') #科目集合
for i in range(0, n):
    name = input("Please enter the name of student {}: ".format(i + 1))
    marks = []   #成绩列表
    for x in subjects:
        marks.append(int(input("enter the makrs of {}: ".format(x))))
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")
