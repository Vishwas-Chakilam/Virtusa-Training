sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
# Slice reversing lists
reversed_words = words[::-1]
# Joining with spaces
new_sentence = " ".join(reversed_words)
print(new_sentence)