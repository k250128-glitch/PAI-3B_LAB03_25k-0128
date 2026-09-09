text = """
machine learning is powerful
machine learning helps analyze data
data science uses machine learning
"""

text = text.lower()
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

most_frequent = max(freq, key=freq.get)

unique_words = set(words)

repeated_words = [word for word, count in freq.items() if count > 1]

print("Word Frequencies:", freq)
print("Most Frequent Word:", most_frequent)
print("Unique Words:", unique_words)
print("Words Appearing More Than Once:", repeated_words)
