
num1 = 10
num2 = 5

add = num1 + num2       # addition
sub = num1 - num2       # subtraction
mul = num1 * num2       # multiplication

# division - the "/" operator ALWAYS returns a float in Python,
# even if the numbers divide evenly (e.g. 10 / 5 gives 2.0, not 2)
# this is different from many other languages where int / int = int
div = num1 / num2

modulo = num1 % num2    # modulo -> returns the remainder of the division 

print("Addition: ", add)          # 15
print("Subtraction: ", sub)       # 5
print("Multiplication: ", mul)    # 50
print("Division: ", div)          # 2.0 (float, even though it's a whole number)
print("Modulo: ", modulo)         # 0 (remainder of 10 / 5)
print(2 ** 3)                     # Exponent operator ** (power) 2**3 = 8

# Floor division "//" gives an int-like whole number result
# (drops the decimal part instead of rounding)
floor_div = num1 // num2
print(floor_div)              # 2
print(type(floor_div))        # <class 'int'>  (since both num1, num2 are int)

# But if EITHER number involved is a float, the result becomes a float
print(10 / 2)     # 5.0  -> float, because "/" always gives float
print(10 // 2)    # 5    -> int, because "//" keeps int when both inputs are int
print(10.0 // 2)  # 5.0  -> float, because one of the inputs was already a float