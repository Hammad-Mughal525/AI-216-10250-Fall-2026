"""Task 9: Clean prediction analysis and realistic batch handling."""
from preprocessing import (
    filter_by_confidence,
    normalize_labels,
    split_complete_records,
)
from analysis import (
    average_confidence,
    count_by_label,
    find_unexpected_labels,
    get_unique_labels,
    top_predictions,
)

MIN_CONFIDENCE = 0.80
ALLOWED_LABELS = {"spam", "ham", "promotion"}
REQUIRED_FIELDS = ("id", "label", "confidence")
TOP_COUNT = 3

initial_predictions = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.41},
    {"id": 4, "label": "spam", "confidence": 0.89},
    {"id": 5, "label": "ham", "confidence": 0.97},
    {"id": 6, "label": "promotion", "confidence": 0.83},
    {"id": 7, "label": "ham", "confidence": 0.58},
]

new_batch = [
    {"id": 8, "label": "Spam", "confidence": 0.91},
    {"id": 9, "label": "ham"},
    {"id": 10, "label": "unknown", "confidence": 0.86},
    {"id": 11, "label": " HAM ", "confidence": 0.66},
]

all_predictions = initial_predictions + new_batch

# Part A: refactored behavior
selected = filter_by_confidence(initial_predictions, MIN_CONFIDENCE)
print("Selected IDs:", [record["id"] for record in selected])
print("Label counts:", count_by_label(initial_predictions))
print("Unique labels:", sorted(get_unique_labels(initial_predictions)))

# Part B: incomplete records are reported and skipped.
complete_records, incomplete_records = split_complete_records(
    all_predictions, REQUIRED_FIELDS
)
skipped_ids = [record["id"] for record in incomplete_records]

normalized_records = normalize_labels(complete_records)

selected_records = filter_by_confidence(normalized_records, MIN_CONFIDENCE)
labels = sorted(get_unique_labels(normalized_records))
label_counts = count_by_label(normalized_records)
unexpected_labels = find_unexpected_labels(
    normalized_records, ALLOWED_LABELS
)
average = average_confidence(normalized_records)
top_records = top_predictions(normalized_records, TOP_COUNT)

summary = {
    "total_records": len(all_predictions),
    "valid_records": len(normalized_records),
    "skipped_ids": skipped_ids,
    "labels": labels,
    "label_counts": label_counts,
    "high_confidence_count": len(selected_records),
    "unexpected_labels": sorted(unexpected_labels),
    "average_confidence": average,
    "top_ids": [record["id"] for record in top_records],
}

print("\n=== Prediction Report ===")
print(f"Total records:          {summary['total_records']}")
print(f"Valid records:          {summary['valid_records']}")
print(f"Skipped (missing data): {summary['skipped_ids']}")
print(f"Labels:                 {summary['labels']}")
print(f"Label counts:           {summary['label_counts']}")
print(f"High confidence (>= 0.8): {summary['high_confidence_count']}")
print(f"Unexpected labels:      {summary['unexpected_labels']}")
print(f"Average confidence:     {summary['average_confidence']:.3f}")
print(f"Top 3 by confidence:    {summary['top_ids']}")

print("Raw label for record 8:", new_batch[0]["label"])

# Basic edge-case checks required by the lab.
assert filter_by_confidence([], MIN_CONFIDENCE) == []
assert average_confidence([]) is None
assert len(filter_by_confidence(
    [{"id": 99, "label": "spam", "confidence": 0.80}],
    MIN_CONFIDENCE
)) == 1
assert new_batch[0]["label"] == "Spam"
