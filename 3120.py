def numberOfSpecialChars(self, word: str) -> int:
    small_letters = set()
    big_letters = set()
    
    for i in word:
        if i.isupper():
            big_letters.add(i)
        else:
            small_letters.add(i)
    
    big_lower = {ch.lower() for ch in big_letters}

    result = len(small_letters & big_lower)
    return result