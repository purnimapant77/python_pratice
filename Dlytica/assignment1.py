#Operator Precedence & Associativity
print("Demonstration of operator precedence & associativity")

#1 Arithmetic Precedence
print("Arithmetic Precedence i.e *,/ before +,-")

print("Without parenthesis:")
result = 2 + 7 * 100
print(f"Result of: 2+7*100 = {result}")  # Expected: 702, multiplication is done first

print("With parenthesis:")
result1 = (2 + 7) * 100
print(f"Result of: (2+7)*100 = {result1}")  # Expected: 900, addition is done first

print("In result without parenthesis multiplication is done first")
print("In result with parenthesis addition is done first")

print("Without parenthesis:")
result = 20 - 8 / 2
print(f"Result of: 20-8/2 = {result}")  # Expected: 16.0, division is done first

print("With parenthesis:")
result1 = (20 - 8) / 2
print(f"Result of: (20-8)/2 = {result1}")  # Expected: 6.0, subtraction is done first

print("In result without parenthesis division is done first")
print("In result with parenthesis subtraction is done first")

#2 Exponential Operator
print("Exponentiation Operator (**)")

print("Without parenthesis:")
result = 2 ** 3 ** 2
print(f"Result of: 2**3**2 = {result}")  # Expected: 512, exponentiation is done right to left

print("With parenthesis:")
result1 = (2 ** 3) ** 2
print(f"Result of: (2**3)**2 = {result1}")  # Expected: 64, left side is calculated first

print("In result without parenthesis exponentiation is done from right to left")
print("In result with parenthesis left side is calculated first")

print("\nExponentiation and Unary Minus")

print("Without parenthesis:")
result2 = -5 ** 2
print(f"Result of: -5**2 = {result2}")  # Expected: -25, exponentiation is done before unary minus

print("With parenthesis:")
result3 = (-5) ** 2
print(f"Result of: (-5)**2 = {result3}")  # Expected: 25, -5 is treated as the base

print("In result without parenthesis exponentiation is done first")
print("In result with parenthesis -5 is taken as the base")

#3 Left to Right Associativity
print("Left to Right Associativity")

print("Without parenthesis:")
result = 100 / 5 * 2
print(f"Result of: 100/5*2 = {result}")  # Expected: 40.0, operations are done left to right

print("With parenthesis:")
result1 = 100 / (5 * 2)
print(f"Result of: 100/(5*2) = {result1}")  # Expected: 10.0, multiplication is done first

print("In result without parenthesis operations are performed from left to right")
print("In result with parenthesis multiplication is done first")

print("\nSubtraction Associativity")

print("Without parenthesis:")
result2 = 10 - 5 - 2
print(f"Result of: 10-5-2 = {result2}")  # Expected: 3, subtraction is done left to right

print("With parenthesis:")
result3 = 10 - (5 - 2)
print(f"Result of: 10-(5-2) = {result3}")  # Expected: 7, subtraction inside parenthesis is done first

print("In result without parenthesis subtraction is done from left to right")
print("In result with parenthesis subtraction inside parenthesis is done first")

print("\nMultiple Division")

print("Without parenthesis:")
result4 = 64 / 4 / 2
print(f"Result of: 64/4/2 = {result4}")  # Expected: 8.0, division is done left to right

print("With parenthesis:")
result5 = 64 / (4 / 2)
print(f"Result of: 64/(4/2) = {result5}")  # Expected: 32.0, division inside parenthesis is done first

print("In result without parenthesis division is done from left to right")
print("In result with parenthesis division inside parenthesis is done first")

#4 Mixed Arithmetic, Comparison and Logical Operators

print("Mixed Arithmetic, Comparison and Logical Operators")

print("Arithmetic before Comparison")
print("Without parenthesis:")
result = 2 + 3 * 4 > 10
print(f"Result of: 2+3*4>10 = {result}")  # Expected: True, arithmetic is done before comparison

print("In this result multiplication is done first, then addition and then comparison")

print("\nComparison before and")
result1 = 5 > 3 and 10 < 20
print(f"Result of: 5>3 and 10<20 = {result1}")  # Expected: True, comparisons are evaluated before and

print("In this result both comparisons are evaluated first and then and is applied")

print("\nand before or")
result2 = True or False and False
print(f"Result of: True or False and False = {result2}")  # Expected: True, and is evaluated before or

print("In this result and is evaluated before or")

print("\nnot before and")
result3 = not True and False
print(f"Result of: not True and False = {result3}")  # Expected: False, not is evaluated before and

print("In this result not is evaluated before and")

print("\nComplex Expression")
x = 5
y = 10

result4 = x * 2 < y and not y > 20 or y == 10
print(f"Result of: x*2<y and not y>20 or y==10 = {result4}")  # Expected: True, arithmetic then comparison then logical operators

print("Arithmetic is done first, then comparison and finally logical operators")