def count_word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    freq = {}
    for x in words:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
    return freq

input_sentence = "the cat and the hat"
result = count_word_frequency(input_sentence)

print(f"Sentence: {input_sentence}")
print(f"word count: {result}")