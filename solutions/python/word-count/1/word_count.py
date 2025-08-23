def count_words(sentence: str) -> dict[str, int]:
    sentence = sentence.lower()
    for char in ',!&@$%^&._:':
        sentence = sentence.replace(char, ' ')
    
    count_dict = {}
    for word in sentence.split():
        word = word.strip("'")
        if word:
            count_dict[word] = count_dict.get(word, 0) + 1
    
    return count_dict