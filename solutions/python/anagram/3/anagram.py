def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word_lower = word.lower()
    length = len(word_lower)
    word_sorted = sorted(word_lower)
    
    return [
        candidate for candidate in candidates
        if (candidate_lower := candidate.lower()) != word_lower 
        and word_sorted == sorted(candidate_lower)
    ]