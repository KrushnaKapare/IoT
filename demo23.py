def function1():
    l1 = [
        [1,2,3,4],
        [10,20,30,40],
        [11,22,33,44]
    ]

    print(l1)
    print("l1 = ",l1)
    print(f"l1 = {l1}")
    for list in l1:
        print(list)

function1()

def function2():
    l1 = [
        [1,2,3,4],
        [5,6,7,8],
        [0,9,8,7]
    ]

    # for l in l1:
    #     print(l)

    for l in l1:
        for e in l:
            print(e, end=" ")
        print("")

function2()

def function3():
    students = [
        [12, "abc", 97.0],
        [13, "xyz", 98.0],
        [11, "qwe", 12.3]
    ]

    print(students)

    for stud in students:
        print(stud)

    for st in students:
        print(f"rollno={st[0]}, name = {st[1]}, marks = {st[2]}")

    for rollno, name, marks in students:
        print(f"rollno = {rollno}, name={name}, marks={marks}")

function3()

