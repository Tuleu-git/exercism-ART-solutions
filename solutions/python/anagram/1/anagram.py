def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word_lower = word.lower()
    length = len(word_lower)
    word_sorted = sorted(word_lower)
    
    result = []
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower == word_lower:
            continue
        if length == len(candidate_lower) and word_sorted == sorted(candidate_lower):
            result.append(candidate)
    
    return result