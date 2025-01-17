from rational_number import RationalNumber

# Create rational numbers
r1 = RationalNumber(3, 4)
r2 = RationalNumber(1, 2)

# Perform arithmetic operations
sum_result = r1 + r2
mul_result = r1 * r2
sub_result = r1 - r2
div_result = r1 / r2

# Display results
print("Sum:", sum_result)        # Output: Sum: 5/4
print("Product:", mul_result)    # Output: Product: 3/8
print("Difference:", sub_result) # Output: Difference: 1/4
print("Quotient:", div_result)   # Output: Quotient: 3/2

# Simplify and represent as float or integer
print("As float:", float(sum_result))  # Output: As float: 1.25
print("As int:", int(sum_result))      # Output: As int: 1
