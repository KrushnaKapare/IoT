# calculator

num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))

print("1.Add\n2.Sub\n3.Mul\n4.Div")
choice = int(input("Enter choice :"))

if choice == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == 4:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("invalid opeartion")
    