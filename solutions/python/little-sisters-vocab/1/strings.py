def add_prefix_un(word: str) -> str:
    return 'un' + word

def make_word_groups(vocab_words: list[str]) -> str:
    final = vocab_words[0]
    for i in range(1, len(vocab_words)):
        final += ' :: ' + vocab_words[0] + vocab_words[i]
    return final

def remove_suffix_ness(word: str) -> str:
    return word[:-4] if not word[:-4].endswith('i') else word[:-5] + 'y'

def adjective_to_verb(sentence: str, index: int) -> str:
    return sentence[:-1].split()[index] + 'en'
