def clean_scores(scores):
    return [score for score in scores if 0 <= score <= 100]
