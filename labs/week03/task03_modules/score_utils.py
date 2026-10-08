def calculate_average(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)

def is_passing(score, passing_score=50):
    return score >= passing_score

def count_above_threshold(scores, threshold):
    return sum(1 for score in scores if score >= threshold)

if __name__ == "__main__":
    sample_scores = [72, 88, 45, 91, 67]
    print(f"Average: {calculate_average(sample_scores):.2f}")
    print("First score passing:", is_passing(sample_scores[0]))
    print("Scores >= 80:", count_above_threshold(sample_scores, 80))
