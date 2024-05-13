def calculate_grade_average(n, grades):
    total_grade = sum(grades)
    average_grade = total_grade / n
    return round(average_grade, 1)

def determine_grade(average_grade):
    if average_grade >= 4.0:
        return "Perfect"
    elif average_grade >= 3.0:
        return "Good"
    else:
        return "Poor"

def main():
    n = int(input())
    grades = list(map(float, input().split()))

    average_grade = calculate_grade_average(n, grades)
    grade_category = determine_grade(average_grade)

    print(average_grade)
    print(grade_category)

if __name__ == "__main__":
    main()