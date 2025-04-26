def word_count(s:str) -> dict:
    words = s.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count("this is a test this is only a test"))
