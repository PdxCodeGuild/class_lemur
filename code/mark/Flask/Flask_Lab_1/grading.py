import random

def assign_grade(score):
    letter_grade = None
    if score > 100 or score < 0:
        return "You did not enter a number between 0 and 100"
    elif score < 60:
        letter_grade = "F"
        return letter_grade
    elif score > 59 and score < 70:
        letter_grade = "D"
        return letter_grade
    elif score > 69 and score < 80:
        letter_grade = "C"
        return letter_grade
    elif score > 79 and score < 90:
        letter_grade = "B"
        return letter_grade
    else:
        letter_grade = "A"
        return letter_grade

def get_rival_score():
    score = random.randint(0,100)
    return score

def compare_scores(user_score, rival_score):
    if user_score > rival_score:
        return "was higher than"
    elif user_score < rival_score:
        return "was less than"
    else:
        return "was equal to"


def compare_and_return_grades(user_score):
    rival_score = get_rival_score()
    user_grade = assign_grade(user_score) + high_mid_low_grade(user_score)
    compare_result = compare_scores(user_score,rival_score)
    rival_grade = assign_grade(rival_score) + high_mid_low_grade(rival_score)
    return rival_score, user_grade, compare_result, rival_grade

def high_mid_low_grade(grade):
    grade_range = grade % 10
    if grade < 54 or grade_range < 4:
        return "-"
    elif (grade > 53 and grade < 57) or (grade_range > 3 and grade_range < 7):
        return ""
    else:
        return "+"