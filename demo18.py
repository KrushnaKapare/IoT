# tuple

def function1():
    t1 =(11,22,33,44,55)

    print(f"len(t1) = {len(t1)}")
    print(f"type(t1) = {type(t1)}")
    print(f"t1 = {t1}")

    print(f"t1[0] = {t1[0]}")
    print(f"t1[2] = {t1[2]}")

    print("t1 using for loop : ")
    for value in t1:
        print(value)

function1()

def function2():
    t = (111,222,333,444,555,222)

    print(f"before len = {len(t)}, t = {t}")
    print(f"count of 222 = {t.count(222)}")
    print(f"index of 33 = {t.index(444)}")

function2()

def function3():
    student = (120, "abc", 98.0)

    print(f"student = {student}")
    print(f"type of student = {type(student)}")

    i = 0
    while i < len(student):
        print(f"student[{i}] = {student[i]} ({type(student[i])})")
        i +=1

function3()