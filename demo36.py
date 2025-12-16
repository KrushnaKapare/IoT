
def toupper(func):
    def inner():
        return func().upper()

    return inner

@toupper
def msg():
    return "KruShna"

print(msg())