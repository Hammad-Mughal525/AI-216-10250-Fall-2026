def calculate_percentage(obtained, total):
    if total <= 0:
        raise ValueError("Total marks must be greater than 0.")
    if obtained < 0:
        raise ValueError("Obtained marks cannot be negative.")
    if obtained > total:
        raise ValueError("Obtained marks cannot be greater than total marks.")
    return (obtained / total) * 100

try:
    obtained = float(input("Enter obtained marks: "))
    total = float(input("Enter total marks: "))
    percentage = calculate_percentage(obtained, total)
except ValueError as error:
    print(f"Invalid input: {error}")
else:
    print(f"Percentage: {percentage:.2f}%")
finally:
    print("Percentage calculation finished.")
