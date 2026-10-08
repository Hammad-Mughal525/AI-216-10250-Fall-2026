# Bugs found:
# 1. total = score should be total += score.
# 2. >= 85 must be checked before >= 50.

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def classify(average):
    if average >= 85:
        return "Excellent"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

scores = [60, 70, 80, 90]
average = calculate_average(scores)
print("Average:", average)
print("Result:", classify(average))
