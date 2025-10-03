number_1 = int(input())
number_2 = int(input())
check_limit = 16
if number_2 - 1 < 16:
    check_limit = number_2 -1
print("=== Challenge 1: Collatz Conjecture ===")
sequence = str(number_1) # sequence starts w/ the first num
steps = 0
current_number = number_1
while current_number > 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = (current_number * 3) + 1
    sequence = sequence + " " + str(current_number)
    steps = steps +1
print(f"Enter starting number: Sequence: {sequence}") 
print(f"Steps: {steps}")
print()
print("=== Challenge 2: Prime Number Checker ===")
print(f"Enter a number: Testing divisors from 2 to {check_limit}...")
is_prime = 1
if number_2 <= 1:
    is_prime = 0
elif number_2 == 2:
    is_prime = 1
else:
    limit = number_2**0.5
    x = 2
    while x <= limit:
        if number_2 % x == 0:
            is_prime = 0
            break
        x = x + 1
if is_prime == 1:
    print(f"{number_2} is prime!")
else:
    print(f"{number_2} is not prime (divisible by {x})")
print()

# Gemini helped to correct mistakes I had made, mainly concerning generating the sequence
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
header = " " * 3 # Corrected by Gemini
y = 1
while y <= 10:
    header = header + f"{y:4}" # Corrected by Gemini
    y = y + 1
print(header) # Corrected by Gemini
z = 1
while z <= 10:
    row = f"{z:2} " # Gemini helped me realize I needed the curly brackets
    f = 1
    while f <= 10:
        product = z * f
        row = row + f"{product:4}"
        f = f + 1
    print(row)
    z = z + 1