"""Task 2: Aliasing, shallow copy, and deep copy"""
import copy

# Part A: aliasing
original_scores = [70, 80, 90]
processed_scores = original_scores
processed_scores.append(100)
print("Aliasing - Original:", original_scores)
print("Aliasing - Processed:", processed_scores)

# Part B: separate list
original_scores = [70, 80, 90]
processed_scores = original_scores.copy()
processed_scores.append(100)
print("Original:", original_scores)
print("Processed:", processed_scores)

# Part C: shallow copy
raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"}
]
shallow_predictions = raw_predictions.copy()
shallow_predictions[0]["label"] = "spam"
print("Raw after shallow copy edit:", raw_predictions)

# Deep copy
raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"}
]
deep_predictions = copy.deepcopy(raw_predictions)
deep_predictions[0]["label"] = "spam"
print("Raw after deep copy edit:", raw_predictions)
print("Deep copy:", deep_predictions)
