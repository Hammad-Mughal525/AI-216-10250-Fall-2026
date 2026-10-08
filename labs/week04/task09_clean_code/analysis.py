"""Analysis functions for prediction records."""


def count_by_label(predictions):
    counts = {}
    for record in predictions:
        label = record["label"]
        counts[label] = counts.get(label, 0) + 1
    return counts


def get_unique_labels(predictions):
    return {record["label"] for record in predictions}


def find_unexpected_labels(predictions, allowed_labels):
    labels = get_unique_labels(predictions)
    return labels - allowed_labels


def average_confidence(predictions):
    if not predictions:
        return None
    return sum(record["confidence"] for record in predictions) / len(predictions)


def top_predictions(predictions, count):
    ordered = sorted(
        predictions,
        key=lambda record: record["confidence"],
        reverse=True
    )
    return ordered[:count]
