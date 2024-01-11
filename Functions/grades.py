
def result_grade(grade):
    if 2 <= score <= 2.99:
        return 'Fail'
    elif 2.99 < score <= 3.49:
        return 'Poor'
    elif 3.49 < score <= 4.49:
        return 'Good'
    elif 4.49 < score <= 5.49:
        return 'Very Good'
    elif 5.49 < score <= 6:
        return 'Excellent'
    else:
        return 'None'


score = float(input())
print(result_grade(score))
