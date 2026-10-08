def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)

def find_highest(scores):
    if not scores:
        return None
    return max(scores)

def count_above_threshold(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count

def classify_average(average):
    if average is None:
        return "No valid data"
    if average >= 85:
        return "Excellent"
    if average >= 70:
        return "Good"
    if average >= 50:
        return "Satisfactory"
    return "Needs Improvement"

scores = [78, 85, 92, 67, 88]
average = calculate_average(scores)
print("Scores:", scores)
print(f"Average: {average:.2f}")
print(f"Highest score: {find_highest(scores)}")
print(f"Scores >= 80: {count_above_threshold(scores, 80)}")
print(f"Classification: {classify_average(average)}")
print("Empty average:", calculate_average([]))
