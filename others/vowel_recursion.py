def count_vowel(n):
    if len(n) == 0:
        return 0
    elif(
        n[0] == "a"
        or n[0] == "e"
        or n[0] == "i"
        or n[0] == "o"
        or n[0] == "u"
        or n[0] == "A"
        or n[0] == "E"
        or n[0] == "I"
        or n[0] == "O"
        or n[0] == "U"
    ):
        return 1 + count_vowel(n[1:])
    else:
        return count_vowel(n[1:])
    

print(count_vowel("hioUon Klam"))