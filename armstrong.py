num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))
print("Armstrong Number" if sum_of_digits == num else "Not an Armstrong Number")
