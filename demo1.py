# temperature = 0.1 + 0.2
# if temperature == 0.3:
#     print("OK")
# else:
#     print("Mismatch")

# if round(0.1+0.2,1)==0.3:
#     print("OK")
# else:
#     print("Mismatch")

# if abs((0.1+0.2) - 0.3) < 0.00001:
#     print("OK2")
# else:
#     print("Mismatch")

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a+b)

print(a-b)