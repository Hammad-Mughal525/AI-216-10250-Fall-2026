"""Task 1: Working with Lists"""
ACCURACY_THRESHOLD = 0.85

accuracies = [0.82, 0.91, 0.87, 0.78, 0.93, 0.85]

print("First:", accuracies[0])
print("Last:", accuracies[-1])
print("Middle four:", accuracies[1:5])

accuracies.append(0.89)
accuracies.extend([0.84, 0.90])

replace_index = accuracies.index(0.78)
accuracies[replace_index] = 0.80

print("Updated:", accuracies)
print("Scores >= 0.85:", sum(score >= ACCURACY_THRESHOLD for score in accuracies))
print("Highest:", max(accuracies))
print("Lowest:", min(accuracies))

sorted_scores = sorted(accuracies, reverse=True)
print("Sorted (high to low):", sorted_scores)
print("Original order kept:", accuracies)

# append([0.84, 0.90]) would add one nested list.
# extend([0.84, 0.90]) adds both scores as separate values.
