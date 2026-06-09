print("*****Student grade analysis system*****")

def letter_grade(score):
    if score>100 or score<0:
        raise ValueError(f"Your marks {score} is invalid, Score should be between 0 to 100")
    if score>=90:
        return "A"
    elif score<90 and score>=80:
        return "B"
    elif score<80 and score>=70:
        return "C"
    elif score<70 and score>=60:
        return "D"
    else:
        return "F"

def analyse(students):
    result = {}
    for name, score in students.items():
        result[name]={
            "score":score,
            "grade":letter_grade(score)
        }
    return result

def summary(results):
    scores  = [info["score"] for info in results.values()]
    average = sum(scores) / len(scores)
    highest = max(results, key=lambda k: results[k]["score"])
    lowest  = min(results, key=lambda k: results[k]["score"])
    counts = {}
    for info in results.values():
        grade = info["grade"]
        counts[grade] = counts.get(grade, 0) + 1
    print(f"\nClass Average : {average:.2f}")
    print(f"Highest Score : {highest} ({results[highest]['score']})")
    print(f"Lowest Score  : {lowest} ({results[lowest]['score']})")
    grade_str = "  ".join(f"{g}={counts.get(g, 0)}" for g in ["A", "B", "C", "D", "F"])
    print(f"Grade Counts  : {grade_str}")

def run(students):
    try:
        results = analyse(students)
        print()
        for name, info in results.items():
            print(f"{name:<6} : {info['score']} → {info['grade']}")
        summary(results)
    except ValueError as e:
        print(f"\nError caught: {e}")
        print("Please fix the invalid score and try again.")

student1 = {
    "Alice": 92, "Bob": 78, "Carol": 85,
    "Dave": 61, "Eve": 55, "Frank": 99
}
run(student1)

student2 = {
    "Alice": 92, "Bob": 78, "Carol": 110
}
run(student2)