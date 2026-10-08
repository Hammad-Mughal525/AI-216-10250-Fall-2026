"""Task 5: Sets for unique labels and validation"""

training_labels = ["spam", "ham", "spam", "promotion", "ham"]
test_labels = ["spam", "ham", "unknown", "promotion"]

training_set = set(training_labels)
test_set = set(test_labels)

print("Unique training labels:", sorted(training_set))
print("In both:", sorted(training_set & test_set))
print("Only in test:", sorted(test_set - training_set))
print("In either:", sorted(training_set | test_set))

# A set expresses union/intersection/difference directly and uses
# hash-based membership checks, making membership checks efficient.
