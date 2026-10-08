"""Task 8: Choosing the right data structure"""

# A: list - order matters
evaluated_models = ["model_a", "model_b", "model_c"]

# B: tuple - fixed image size
fixed_image_size = (224, 224)

# C: dictionary - meaningful field names
model_config = {
    "name": "spam_classifier",
    "threshold": 0.80,
    "version": 2,
    "debug_status": "ready"
}

# D: set - unique labels
unique_labels = {"spam", "ham", "promotion"}

# E: list of dictionaries - many structured prediction records
prediction_records = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72}
]

# F: set comparison - allowed vs received labels
allowed_labels = {"spam", "ham", "promotion"}
received_labels = {"spam", "ham", "unknown"}
unexpected_labels = received_labels - allowed_labels

print("A - Evaluated models:", evaluated_models)
print("B - Fixed image size:", fixed_image_size)
print("C - Model config:", model_config)
print("D - Unique labels:", sorted(unique_labels))
print("E - Prediction records:", prediction_records)
print("F - Unexpected labels:", sorted(unexpected_labels))
