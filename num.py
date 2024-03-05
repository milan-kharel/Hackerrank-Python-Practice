import numpy

N, M = map(int, input().split())

a = numpy.array([list(map(int, input().split())) for n in range(N)])

b = numpy.array([list(map(int, input().split())) for n in range(N)])

# Perform various operations on the arrays

# Addition: Element-wise addition of arrays 'a' and 'b'
print(numpy.add(a, b))

# Subtraction: Element-wise subtraction of array 'b' from array 'a'
print(numpy.subtract(a, b))

# Multiplication: Element-wise multiplication of arrays 'a' and 'b'
print(numpy.multiply(a, b))

# Division: Element-wise floor division of array 'a' by array 'b'
print(a // b)

# Modulus (Remainder): Element-wise modulus of array 'a' by array 'b'
print(numpy.mod(a, b))

# Exponentiation: Element-wise exponentiation of array 'a' to the power of array 'b'
print(numpy.power(a, b))
