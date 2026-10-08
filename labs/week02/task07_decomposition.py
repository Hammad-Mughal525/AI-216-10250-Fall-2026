# Problem:
# Monitor AI service response times and classify each request.

# Inputs:
response_times = [250, 420, 180, 900, 310, 1500, 275]

# Rules:
# Fast       -> <= 300 ms
# Acceptable -> 300 < time <= 700 ms
# Slow       -> > 700 ms

# Repetition:
# Check every response time using a for loop.

# Outputs:
# Print the category of each request and a final summary.

fast_count = 0
acceptable_count = 0
slow_count = 0

for response_time in response_times:
    if response_time <= 300:
        category = "Fast"
        fast_count += 1
    elif response_time <= 700:
        category = "Acceptable"
        acceptable_count += 1
    else:
        category = "Slow"
        slow_count += 1

    print(f"Response time: {response_time} ms - {category}")

print("\nFinal Summary:")
print(f"Fast: {fast_count}")
print(f"Acceptable: {acceptable_count}")
print(f"Slow: {slow_count}")
