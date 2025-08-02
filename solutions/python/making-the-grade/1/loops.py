def round_scores(student_scores: list[float | int]) -> list[int]:
    for index, score in enumerate(student_scores):
        student_scores[index] = round(score)
    return student_scores

def count_failed_students(student_scores: list[int]) -> int:
    i = 0
    for score in student_scores:
        if score <= 40:
            i += 1
    return i

def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    list_of_best = []
    for score in student_scores:
        if score >= threshold:
            list_of_best.append(score)
    return list_of_best

def letter_grades(highest: int) -> list[int]:
    return [41, 41 + (highest - 40) // 4, 41 + (highest - 40) // 4 * 2, 41 + (highest - 40) // 4 * 3]

def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    ranking = []
    for index, name in enumerate(student_names):
        ranking.append(f'{index +1}. {name}: {student_scores[index]}')
    return ranking

def perfect_score(student_info: list[list[str | int]]) -> list[str | int]:
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []
