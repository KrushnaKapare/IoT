def function1():
    students=[
          (2, "abc", 97.0),
        (9, "xyz", 89.5),
        (15, "pqr", 91.7)
    ]

    print(students)

    for stud in students:
        print(stud)

    for stud in students:
        print(f"stud[0]= {stud[0]}, stud[1]={stud[1]}, stud[2]={stud[2]}")

function1()

def function2():
    students =[
        {'rollno':2, 'name':"abc",'marks':97.9},
        {'rollno':3, 'name':"qee",'marks':93.9},
        {'rollno':4, 'name':"dde",'marks':92.9},

    ]

    print(students)
    for stud in students:
        print(stud)

    for stud in students:
        print(stud.values())

function2()