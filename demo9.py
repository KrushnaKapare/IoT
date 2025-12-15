# loops

num = int(input("Enter number :"))

# i = 1
# print(f"table pf {num} :")
# while i <= 10:
#     print(i*num)
#     i+=1

fact = 1
i = 1
while i<= num:
    fact *= i
    i += 1
else:
    print("condition is false")

print(f"{num}! = {fact}")
