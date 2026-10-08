from score_utils import calculate_average, is_passing, count_above_threshold

scores = [72, 88, 45, 91, 67]
print("Average:", f"{calculate_average(scores):.2f}")
print("First score passing:", is_passing(scores[0]))
print("Scores >= 80:", count_above_threshold(scores, 80))
