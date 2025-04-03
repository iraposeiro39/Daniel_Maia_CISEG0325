#!/bin/python3
# Vars
num1 = 0
num2 = 0
num3 = 0

# Input
num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))
num3 = int(input("Introduza o terceiro número: "))

# MENOR
if num1 < num2 and num1 < num3:
    print(f"O menor número é o primeiro ({num1})")
elif num2 < num1 and num2 < num3:
    print(f"O menor número é o segundo ({num2})")
else:
    print(f"O menor número é o terceiro ({num3})")

# MAIOR
if num1 > num2 and num1 > num3:
    print(f"O maior número é o primeiro ({num1})")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é o segundo ({num2})")
else:
    print(f"O maior número é o terceiro ({num3})")

# MEIO
if (num1 < num3 and num1 > num2) or (num1 > num3 and num1 < num2):
    print(f"O número do meio é o primeiro ({num1})")
elif (num2 < num3 and num2 > num1) or (num2 > num3 and num2 < num1):
    print(f"O número do meio é o segundo ({num2})")
else:
    print(f"O número do meio é o terceiro ({num3})")
