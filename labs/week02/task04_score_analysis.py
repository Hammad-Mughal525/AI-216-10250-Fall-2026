scores = [0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79]
threshold = 0.85

meeting_target = 0
below_target = 0
total_score = 0

if len(scores) == 0:
    print("No scores available for analysis.")
else:
    for score in scores:
        total_score += score

        if score >= threshold:
            meeting_target += 1
        else:
            below_target += 1

    average_score = total_score / len(scores)
    percentage_meeting_target = (meeting_target / len(scores)) * 100

    print(f"Meeting target (>= {threshold}): {meeting_target}")
    print(f"Below target: {below_target}")
    print(f"Average score: {average_score:.2f}")
    print(f"Percentage meeting target: {percentage_meeting_target:.2f}%")

# This logic could later be placed inside a reusable function
# because the same score analysis may be needed for many datasets.
