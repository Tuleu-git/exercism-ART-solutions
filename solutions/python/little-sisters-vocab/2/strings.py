def add_prefix_un(word: str) -> str:
    return 'un' + word

def make_word_groups(vocab_words: list[str]) -> str:
    final_list = [w := vocab_words.pop(0)] + [w + word for word in vocab_words]
    return ' :: '.join(final_list)

def remove_suffix_ness(word: str) -> str:
    return word[:-4] if not word[:-4].endswith('i') else word[:-5] + 'y'

def adjective_to_verb(sentence: str, index: int) -> str:
    return sentence[:-1].split()[index] + 'en'
