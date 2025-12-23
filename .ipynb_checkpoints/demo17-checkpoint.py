# list

def function1():
    mylist = [11,22,33,44,55]
    print(f"len(mylist) = {len(mylist)}")
    print(f"type(mylist) = {type(mylist)}")
    print(f"mylist = {mylist}")

    print(f"mylist[0] = {mylist[0]}")
    print(f"mylist[1] = {mylist[2]}")

    print("mylist using for loop :")
    for value in mylist:
        print(value)

function1()

def function2():
    l = [111,222,333,444,555]
    print(f"Before len = {len(l)}, l = {l}")

    l.append(100)
    l.insert(1,100)

    l.pop()
    l.remove(444)
    l.reverse()
    #l.clear()
    print(f"index of 222 ={l.index(222)}")

    print(f"after len = {len(l)}, l = {l}")

function2()

def function3():
    student = [120, "krushna", 98.0]

    print(f"list = {student}")
    print(f"type of student = {type(student)}")

    i = 0
    while i < len(student):
        print(f"student[{i}] = {student[i]} ({type(student[i])})")
        i += 1

function3()