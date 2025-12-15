# for loop 

string = "sunbeam"

print("string = ",end=" ")

for character in string:
    print(character, end="")
else:
    print("")

print(f"length of string = {len(string)}")

length = 0
for ch in string:
    length += 1

print(f"length of string using for loop : {length}")

