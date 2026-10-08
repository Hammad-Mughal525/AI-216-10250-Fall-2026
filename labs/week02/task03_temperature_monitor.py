temperatures = [21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]

below_normal_count = 0
normal_count = 0
high_count = 0

for temperature in temperatures:
    if temperature < 15:
        category = "Below Normal"
        below_normal_count += 1
    elif temperature <= 30:
        category = "Normal"
        normal_count += 1
    else:
        category = "High"
        high_count += 1

    print(f"Temperature: {temperature:.1f}°C - {category}")

print("\nFinal Summary:")
print(f"Below Normal: {below_normal_count}")
print(f"Normal: {normal_count}")
print(f"High: {high_count}")

# Boundary test:
# If 15.0 and 30.0 are added, both are counted as Normal.
