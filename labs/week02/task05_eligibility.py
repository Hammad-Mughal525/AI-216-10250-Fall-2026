def check_eligibility(age, programming_score, prerequisite_completed):
    eligible = True

    if age < 18:
        eligible = False
        print("- Age requirement not met")

    if programming_score < 60:
        eligible = False
        print("- Programming score requirement not met")

    if not prerequisite_completed:
        eligible = False
        print("- Prerequisite course not completed")

    if eligible:
        print("Eligible")
    else:
        print("Not eligible")


# Applicant 1
print("Applicant 1:")
check_eligibility(19, 72, True)

# Applicant 2
print("\nApplicant 2:")
check_eligibility(18, 60, True)

# Applicant 3
print("\nApplicant 3:")
check_eligibility(17, 55, False)
