"""Task 3: Tuples for fixed data"""

image_size = (224, 224)
model_result = ("baseline_cnn", 0.91)

width, height = image_size
model_name, accuracy = model_result

print(f"Image size: {width} x {height}")
print(f"Model: {model_name} | Accuracy: {accuracy}")


def summarize_scores(scores):
    if not scores:
        return None
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)
    return minimum, maximum, average


summary = summarize_scores([72, 88, 91, 67])
minimum, maximum, average = summary
print(f"Minimum: {minimum} | Maximum: {maximum} | Average: {average}")

empty_summary = summarize_scores([])
print("Empty:", empty_summary)

input_models = {
    (224, 224): "resnet50",
    (299, 299): "inception_v3",
    (384, 384): "vit_base"
}
print("Model for 299x299:", input_models[(299, 299)])

try:
    invalid_models = {[224, 224]: "resnet50"}  # lists cannot be dictionary keys
except TypeError as error:
    print(f"TypeError: {error}")

# Tuples are immutable/hashable when their contents are hashable, so they can
# be dictionary keys. Lists are mutable and therefore cannot be dictionary keys.
