def calculate_percentage(obtained, total):
    if total == 0:
        return 0
    return (obtained / total) * 100


def is_passing(score, passing_score):
    return score >= passing_score


def count_values_above_threshold(values, threshold):
    count = 0

    for value in values:
        if value >= threshold:
            count += 1

    return count


print(calculate_percentage(423, 500))
print(is_passing(50, 50))
print(is_passing(49, 50))
print(count_values_above_threshold(
    [0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79],
    0.85
))
