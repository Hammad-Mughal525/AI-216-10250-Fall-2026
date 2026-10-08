class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores.copy()

    def clean(self):
        self.scores = [score for score in self.scores if 0 <= score <= 100]

    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        return sum(1 for score in self.scores if score >= threshold)

    def summary(self):
        if not self.scores:
            return {"count": 0, "average": None, "highest": None, "lowest": None}
        return {
            "count": len(self.scores),
            "average": self.average(),
            "highest": max(self.scores),
            "lowest": min(self.scores)
        }

raw_scores = [78, -5, 110, 67, 90, 88]
analyzer = ScoreAnalyzer(raw_scores)
analyzer.clean()
print("Cleaned:", analyzer.scores)
print(f"Average: {analyzer.average():.2f}")
print("Count >= 80:", analyzer.count_above(80))
print("Summary:", analyzer.summary())
print("Empty summary:", ScoreAnalyzer([]).summary())
