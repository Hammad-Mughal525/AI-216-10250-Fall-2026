"""Preprocessing functions for prediction records."""


def filter_by_confidence(predictions, min_confidence):
    return [
        record for record in predictions
        if record["confidence"] >= min_confidence
    ]


def split_complete_records(predictions, required_fields):
    complete = []
    incomplete = []
    for record in predictions:
        if all(field in record for field in required_fields):
            complete.append(record)
        else:
            incomplete.append(record)
    return complete, incomplete


def normalize_labels(predictions):
    normalized = []
    for record in predictions:
        copied_record = record.copy()
        copied_record["label"] = copied_record["label"].strip().lower()
        normalized.append(copied_record)
    return normalized
