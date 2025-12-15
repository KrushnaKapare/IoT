def function1():
    str ="""This is our first function
            in python"""                # multi line string
    print(str)

function1()

def function2(param):
    print(f"param = {param}")
    print(f"type(param) = {type(param)}")

function2(10)
function2('krushna')
function2(3.14)
function2(False)

def function3(num1,num2):
    return num1 + num2

ret = function3(10,20)
ret = function3("krus","hna")
ret = function3(20.5,20.5)
print(f"sum = {ret} ({type(ret)})")

