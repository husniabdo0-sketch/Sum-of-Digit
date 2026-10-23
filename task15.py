number = int(input("Enter a whole number: "))
number = abs(number)  # Treat a leading minus sign as a sign, not a digit.
digit_sum = 0

# Get the last digit with modulo 10, then remove it with integer division.
while number > 0:
    digit_sum += number % 10
    number //= 10

# For input 0, the loop does not run and the sum stays 0.
print("Sum of digits:", digit_sum)