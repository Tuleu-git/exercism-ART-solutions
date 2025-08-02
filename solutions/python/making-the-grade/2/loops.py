def round_scores(student_scores: list[float | int]) -> list[int]:
    return [round(score) for score in student_scores]
    # or: list(map(lambda x: round(x), student_scores))

def count_failed_students(student_scores: list[int]) -> int:
    return sum([1 for score in student_scores if score <= 40])
    # or: return len([score for score in student_scores if score <= 40])

def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    return [score for score in student_scores if score >= threshold]

def letter_grades(highest: int) -> list[int]:
    step = (highest - 40) // 4
    return [41 + step * i for i in range(4)]

def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    return [f'{index}. {name}: {score}' for index, (name, score) in enumerate(zip(student_names, student_scores), start = 1)]

def perfect_score(student_info: list[list[str | int]]) -> list[str | int]:
    return next(([name, score] for name, score in student_info if score == 100), [])
