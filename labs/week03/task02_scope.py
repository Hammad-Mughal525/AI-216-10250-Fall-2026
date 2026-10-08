score = 90

def show_score():
    score = 70
    print("Inside function:", score)

show_score()
print("Outside function:", score)

def is_qualified(score, threshold):
    return score >= threshold

print("80, 85:", is_qualified(80, 85))
print("85, 85:", is_qualified(85, 85))
print("90, 85:", is_qualified(90, 85))
