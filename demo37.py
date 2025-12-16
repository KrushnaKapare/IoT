
def change_case(n):
    def change_case(func):
        def inner():
            if n == 1:
                return func().upper()
            else:
                return func().lower()
        return inner
    return change_case

@change_case(3)
def msg():
    return "SunBeam"

print(msg())        
